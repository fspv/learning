import contextlib
import textwrap
from typing import Iterator, List, Tuple, cast

import eth_utils
import solcx  # type: ignore
import web3
from web3.eth import ChecksumAddress, HexStr, Wei


@contextlib.contextmanager
def log_address_info(
    client: web3.Web3, addresses: List[web3.eth.ChecksumAddress]
) -> Iterator[None]:
    for when in ["before", "after"]:
        for address in addresses:
            print(
                textwrap.dedent(
                    f"""
                    Account {address!s} [{when}]:
                        balance {client.eth.get_balance(address)!s}
                        tx count: {client.eth.get_transaction_count(address)!s}
                    """
                )
            )

        if when == "before":
            yield


def compile(source: str, file: str, name: str) -> Tuple[str, str]:
    spec = {
        "language": "Solidity",
        "sources": {file: {"urls": [source]}},
        "settings": {
            "optimizer": {"enabled": True},
            "outputSelection": {"*": {"*": ["metadata", "evm.bytecode", "abi"]}},
        },
    }
    out = solcx.compile_standard(spec, allow_paths=".")

    abi = out["contracts"][file][name]["abi"]
    bytecode = out["contracts"][file][name]["evm"]["bytecode"]["object"]

    return abi, bytecode


def get_client() -> web3.Web3:
    client = web3.Web3(web3.HTTPProvider("http://127.0.0.1:7545"))

    if not client.isConnected():
        print("Not connected")
        raise RuntimeError("Not connected")

    client.middleware_onion.inject(web3.middleware.geth_poa_middleware, layer=0)
    print(f"Connected: {client.clientVersion}")

    return client


def test() -> None:
    client = get_client()

    abi, bytecode = compile("test.sol", "test.sol", "Faucet")

    gas_price = client.eth.generate_gas_price() or 0
    print(f"Gas price: {gas_price}")

    # Other way: client.eth.get_block("latest")
    latest_block = lambda: web3.eth.Eth(client).blockNumber
    print(f"Latest block: {latest_block()}")

    my_address = client.eth.accounts[0]

    print(f"My address: {my_address}")

    client.eth.default_account = my_address

    temp = client.eth.contract(bytecode=bytecode, abi=abi)

    # Submit the transaction that deploys the contract
    tx_hash = temp.constructor().transact()

    # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = client.eth.wait_for_transaction_receipt(tx_hash)

    faucet_address: ChecksumAddress = cast(
        ChecksumAddress, tx_receipt.contractAddress  # type: ignore
    )

    print(f"Contract address: {faucet_address}")

    with log_address_info(client, [my_address, faucet_address]):
        pass

    if not faucet_address:
        raise ValueError("Faucet address should be defined")

    # Top up contract
    print("Top up #1")

    with log_address_info(client, [my_address, faucet_address]):
        txn_hash = web3.eth.Eth(client).send_transaction(
            {"to": faucet_address, "from": my_address, "value": Wei(12345)}
        )
        tx_receipt = client.eth.wait_for_transaction_receipt(txn_hash)

    # Get the mined transaction
    faucet = client.eth.contract(address=faucet_address, abi=abi)

    print("Top up #2")

    with log_address_info(client, [my_address, faucet_address]):
        txn_hash = web3.eth.Eth(client).send_transaction(
            {"to": faucet_address, "from": my_address, "value": Wei(12312300)}
        )
        tx_receipt = client.eth.wait_for_transaction_receipt(txn_hash)

    # Execute contract function
    print("Withdraw money")

    with log_address_info(client, [my_address, faucet_address]):
        txn_hash = faucet.functions.withdraw(Wei(12311)).transact({"from": my_address})

        gas_estimation = faucet.functions.withdraw(Wei(12311)).estimateGas()
        print("Gas estimation: ", gas_estimation)
        print(
            "Transaction cost: ",
            eth_utils.from_wei(gas_estimation * gas_price, "ether"),
        )

        tx_receipt = client.eth.wait_for_transaction_receipt(txn_hash)

        withdrawal_events = faucet.events.Withdrawal.createFilter(
            fromBlock=latest_block() - 100, toBlock=latest_block()
        )
        print("Withdrawal event logs: ", withdrawal_events.get_all_entries())
        deposit_events = faucet.events.Deposit.createFilter(
            fromBlock=latest_block() - 100, toBlock=latest_block()
        )
        print("Deposit event logs: ", deposit_events.get_all_entries())

    # Test sending between accounts
    print("Send money to faucet address")

    with log_address_info(client, [my_address, faucet_address]):
        client.eth.send_transaction(
            {
                "from": my_address,
                "to": faucet_address,
                "value": Wei(eth_utils.to_wei(0.01, "ether")),
            }
        )

    print("Send no money to faucet address, with no data")

    with log_address_info(client, [my_address, faucet_address]):
        txn_hash = client.eth.send_transaction(
            {
                "from": my_address,
                "to": faucet_address,
                "value": Wei(0),
                "data": b"",
            }
        )
        tx_receipt = client.eth.wait_for_transaction_receipt(txn_hash)

    # print("Send no money to faucet address, but some data")

    # with log_address_info(client, [my_address, faucet_address]):
    #    txn_hash = client.eth.send_transaction(
    #        {
    #            "from": my_address,
    #            "to": faucet_address,
    #            "value": Wei(0),
    #            "data": b"0x1234",
    #        }
    #    )
    #    tx_receipt = client.eth.wait_for_transaction_receipt(txn_hash)


def test_nft() -> None:
    client = get_client()

    abi, bytecode = compile("NFT.sol", "NFT.sol", "ExampleNFT")

    my_address = client.eth.accounts[0]

    client.eth.default_account = my_address

    temp = client.eth.contract(bytecode=bytecode, abi=abi)

    # Submit the transaction that deploys the contract
    tx_hash = temp.constructor().transact()

    # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = client.eth.wait_for_transaction_receipt(tx_hash)

    contract_address: ChecksumAddress = cast(
        ChecksumAddress, tx_receipt.contractAddress  # type: ignore
    )
    # contract_address = "0x7F9Fd6aA0da00b115d6c8b1A6b4EfAc2Ec7a6C2c"
    contract = client.eth.contract(address=contract_address, abi=abi)

    txn_hash = contract.functions.mintNFT(
        client.eth.accounts[1],
        "https://gateway.pinata.cloud/ipfs/QmQZ6i1Ac5UWV2otPL69HwMVwo3Ed7Saeivg6aAgvQygrN",
    ).transact({"from": my_address})

    tx_receipt = client.eth.wait_for_transaction_receipt(txn_hash)


def main() -> None:
    test_nft()


if __name__ == "__main__":
    main()
