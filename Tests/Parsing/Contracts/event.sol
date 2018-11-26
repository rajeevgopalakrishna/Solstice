pragma solidity ^0.4.24;

contract Test {

  event LogEvent(address sentTo, uint amount);

  function logger() {
    emit LogEvent(msg.sender, 0);
  }
}
