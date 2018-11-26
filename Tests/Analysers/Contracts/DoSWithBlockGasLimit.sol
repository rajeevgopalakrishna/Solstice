// From https://consensys.github.io/smart-contract-best-practices/known_attacks/#dos-with-block-gas-limit
contract Auction {
  struct Payee {
    address addr;
    uint256 value;
  }
  
  Payee[] payees;
  uint256 nextPayeeIndex;
  
  function payOut() {
    uint256 i = nextPayeeIndex;
    while (i < payees.length && msg.gas > 200000) {
      payees[i].addr.send(payees[i].value);
      i++;
    }
    nextPayeeIndex = i;
  }
}
