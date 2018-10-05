pragma solidity ^0.4.24;

contract FunctionDefinitionTest {

  uint a = 0;
  
  function foo() public {
  }

  function bar() private {
    a++;
  }
}
