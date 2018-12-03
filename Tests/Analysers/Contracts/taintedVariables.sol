pragma solidity ^0.4.24;

contract TestTaintedVariables {

  function foo(address addr, uint i) {
    address a;
    uint j;
    uint k;
    a = addr;
    j = k + 1;
    k = i;
    j = k;
  }
}
