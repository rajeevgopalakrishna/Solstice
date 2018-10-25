pragma solidity ^0.4.24;

contract DefaultVisibilityTest {

  uint a = 0;
  uint internal b = 0;
  
  function foo() {
    a++;
  }

  function bar() public {
    b++;
  }

}
