pragma solidity ^0.4.24;

contract TestWhile {
  uint i = 2;

  function test_while() {
    while (i > 0) {
      i--;
    }
  }
  
}
