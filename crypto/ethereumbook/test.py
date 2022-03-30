from typing import Optional, Tuple, cast

import solcx  # type: ignore
import web3
from web3.eth import ChecksumAddress, Wei


def compile(source: str, file: str) -> Tuple[str, str]:
    spec = {
        "language": "Solidity",
        "sources": {file: {"urls": [source]}},
        "settings": {
            "optimizer": {"enabled": True},
            "outputSelection": {"*": {"*": ["metadata", "evm.bytecode", "abi"]}},
        },
    }
    out = solcx.compile_standard(spec, allow_paths=".")

    abi = out["contracts"]["test.sol"]["Faucet"]["abi"]
    bytecode = out["contracts"]["test.sol"]["Faucet"]["evm"]["bytecode"]["object"]

    return abi, bytecode


def main() -> None:
    abi, bytecode = compile("test.sol", "test.sol")

    client = web3.Web3(web3.HTTPProvider("http://127.0.0.1:8545"))

    if client.isConnected():
        client.middleware_onion.inject(web3.middleware.geth_poa_middleware, layer=0)
        print(f"Connected: {client.clientVersion}")
    else:
        print("Not connected")
        return

    print(f'Latest block: {client.eth.get_block("latest")}')

    my_address = client.eth.accounts[0]

    print(f"My address: {my_address}")
    print(f"My balance: {client.eth.get_balance(my_address)}")

    client.eth.default_account = my_address

    temp = client.eth.contract(bytecode=bytecode, abi=abi)

    print(f"Contract: {temp}")

    # Submit the transaction that deploys the contract
    tx_hash = temp.constructor().transact()

    # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = client.eth.wait_for_transaction_receipt(tx_hash)

    faucet_address: Optional[ChecksumAddress] = cast(
        Optional[ChecksumAddress], tx_receipt.contractAddress  # type: ignore
    )

    if not faucet_address:
        raise ValueError("Faucet address should be defined")

    # Top up contract
    print("Top up #1")

    txn_hash = web3.eth.Eth(client).send_transaction(
        {"to": faucet_address, "from": my_address, "value": Wei(12345)}
    )
    tx_receipt = client.eth.wait_for_transaction_receipt(txn_hash)

    print(f"My balance: {client.eth.get_balance(my_address)}")
    print(f"Contract balance: {client.eth.get_balance(faucet_address)}")

    # Get the mined transaction
    faucet = client.eth.contract(address=faucet_address, abi=abi)

    print("Top up #2")

    txn_hash = web3.eth.Eth(client).send_transaction(
        {"to": faucet_address, "from": my_address, "value": Wei(123123)}
    )
    tx_receipt = client.eth.wait_for_transaction_receipt(txn_hash)

    print(f"My balance: {client.eth.get_balance(my_address)}")
    print(f"Contract balance: {client.eth.get_balance(faucet_address)}")

    # Execute contract function
    print("Withdraw money")

    txn_hash = faucet.functions.withdraw(Wei(12311)).transact({"from": my_address})
    tx_receipt = client.eth.wait_for_transaction_receipt(txn_hash)

    print(f"My balance: {client.eth.get_balance(my_address)}")
    print(f"Contract balance: {client.eth.get_balance(faucet_address)}")


if __name__ == "__main__":
    main()
