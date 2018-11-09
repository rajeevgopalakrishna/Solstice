pragma solidity ^0.4.24;

contract TestDefUse {

  uint a = 0;
  
  struct Data {
    uint st_i;
    string st_str;
  }

  mapping(address => uint) balances;
  
  function bar(uint k) returns (uint) {
    return k+1;
  }
  
  function foo(uint i) returns (uint) {
    Data data;
    uint j;
    a = i + 1;
    a++;
    j = i - 1;
    a = (a + i) + j;
    i = a + i + j + (msg.value);

    if (a > 0) {
      i++;
    }

    j = bar(a);

    while (j < 10) {
      a++;
      j--;
    }

    data.st_i = j;

    balances[msg.sender] = j;
    balances[address(i)] = a;
  }
}
