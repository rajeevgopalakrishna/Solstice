pragma solidity ^0.4.24;

contract Test {
  uint i = 2;

  function test_ifThenElse() {
    if (i < 2) {
      i++;
    }
    else {
      i--;
    }
  }
  
}
