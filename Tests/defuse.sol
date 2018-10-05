pragma solidity ^0.4.24;

contract TestDefUse {

  uint a = 0;
  
  function foo(uint i) returns (uint) {
    uint j;
    a = i + 1;
    a++;
    j = i - 1;
    a = (a + i) + j;
    i = a + i + j + (msg.value);
  }

}
