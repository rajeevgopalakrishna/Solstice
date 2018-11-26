pragma solidity ^0.4.24;

contract Test {

  address public owner;
  
    constructor () {
       owner = msg.sender;
    }

    modifier onlyOwner() {
        if (msg.sender != owner) throw;
        _;
    }

    function foo() onlyOwner {
    }
}
