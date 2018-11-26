pragma solidity ^0.4.24;

contract Contract1 {

  uint a = 0;
  
  function foo(uint i) returns (uint) {
    a = a + i;
    return(a);
  }

  function bar() {
    foo(10);
  }
}


contract Contract2 {

  uint a = 0;
  
  function foo(uint i) returns (uint) {
    a = a + i;
    return(a);
  }

  function bar() {
    foo(10);
  }
}
