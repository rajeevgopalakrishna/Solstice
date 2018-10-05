pragma solidity ^0.4.24;

contract FunctionMutabilityTest {

  uint a;
  
  function foo() view returns (uint) {
    return(a);
  }

  function bar() pure returns (uint) {
    return(10);
  }
}
