pragma solidity ^0.4.24;

contract TestFor {
  uint i = 2;

  function test_for() {
    for(uint j=0; j<10; j++) {
      i++;
    }
  }
  
}
