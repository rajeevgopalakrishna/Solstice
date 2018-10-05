pragma solidity ^0.4.24;

contract ExceptionsTest {

  uint a = 0;
  
  function foo(uint i) public {
    uint c;
    require(i >= 0);
    c = a + i;
    assert(c >= a);
    if (c == a) {
      revert();
    }
  }

}
