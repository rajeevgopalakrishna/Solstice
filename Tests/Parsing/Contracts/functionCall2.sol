pragma solidity ^0.4.24;

contract FunctionCallTest {

  function hexstrToBytes(string _hexstr, uint len) public pure {
    require(len % 2 == 0);
    
    string memory s;
    string memory r;
    uint p = parseInt16Char(s) * 16 + parseInt16Char(r);
  }

  // @dev Parses a hexchar, like 'a', and returns its hex value, in this case 10
  function parseInt16Char(string _char) public pure returns (uint) {
    bytes memory bresult = bytes(_char);
    // bool decimals = false;
    if ((bresult[0] >= 48) && (bresult[0] <= 57)) {
      return uint(bresult[0]) - 48;
    } else if ((bresult[0] >= 65) && (bresult[0] <= 70)) {
      return uint(bresult[0]) - 55;
    } else if ((bresult[0] >= 97) && (bresult[0] <= 102)) {
      return uint(bresult[0]) - 87;
    } else {
      revert();
    }
  }

}
