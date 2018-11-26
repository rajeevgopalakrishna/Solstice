pragma solidity ^0.4.24;

contract FunctionCallTest {

  uint a = 0;
  
  function foo(uint i) returns (uint) {
    a = a + i;
    return(a);
  }

  function bar() {
    foo(10);
  }
}
