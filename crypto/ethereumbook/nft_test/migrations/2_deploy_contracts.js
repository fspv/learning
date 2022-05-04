var NFT = artifacts.require("NFT");

module.exports = function(deployer) {
    deployer.deploy(NFT);
    // Additional contracts can be deployed here
};
