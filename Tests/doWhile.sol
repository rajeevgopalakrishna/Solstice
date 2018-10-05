pragma solidity ^0.4.24;

contract Test {
  uint i = 2;

  function test_doWhile() {
    do {
      i--;
    } while (i > 0);
  }
  
}
