pragma solidity ^0.4.24;

contract Contract1 {

  uint a = 0;
  address owner;
  uint value;
  
  constructor() {
    owner = msg.sender;
  }
  
  function foo(uint i) returns (uint) {
    uint j;
    a = a + i + j;
    return(a);
  }

  function () payable {
    value = msg.value;
  }
}


contract Contract2 {

  uint a = 0;
  address owner;

  constructor() {
    owner = msg.sender;
  }
  
  function foo(uint i) returns (uint) {
    a = a + i;
    return(a);
  }

  function bar() {
    foo(10);
  }
}
