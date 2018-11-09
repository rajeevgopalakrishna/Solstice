pragma solidity ^0.4.24;

contract SelfDestruct {

  address owner;
  
  constructor() {
    owner = msg.sender;
  }

  function kill() {
    if (msg.sender == owner)
      selfdestruct(owner);
  }

  function unprotectedKill() {
    selfdestruct(owner);
  }
}
