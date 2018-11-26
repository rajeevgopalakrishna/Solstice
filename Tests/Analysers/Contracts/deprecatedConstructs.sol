// From https://github.com/SmartContractSecurity/SWC-registry/blob/master/test_cases/timestamp_dependence/timed_crowdsale.sol
pragma solidity ^0.4.24;

contract TimedCrowdsale {
  // Sale should finish exactly at January 1, 2019
  function isSaleFinished() view public returns (bool) {
    return block.timestamp >= 1546300800;
  }
}

// From https://solidity.readthedocs.io/en/develop/security-considerations.html#tx-origin
// THIS CONTRACT CONTAINS A BUG - DO NOT USE
contract TxUserWallet {
    address owner;

    constructor() public {
        owner = msg.sender;
    }

    function transferTo(address dest, uint amount) public {
        require(tx.origin == owner);
        dest.transfer(amount);
    }
}
