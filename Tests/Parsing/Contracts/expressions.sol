pragma solidity ^0.4.24;

contract TestExpressions {

  uint a = 0;
  
  function foo(uint i) returns (uint) {
    a = a + i;
    a = a * i;
    a++;
    a--;
    a = (a - 10) ** (1 + 1);
    a = a ** 2;
  }

}
