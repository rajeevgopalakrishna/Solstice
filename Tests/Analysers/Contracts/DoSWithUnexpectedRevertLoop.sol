// From https://consensys.github.io/smart-contract-best-practices/known_attacks/#dos-with-unexpected-revert
contract Auction {

  address[] private refundAddresses;
  mapping (address => uint) public refunds;
  
  // bad
  function refundAll() public {
    for(uint x; x < refundAddresses.length; x++) { // arbitrary length iteration based on how many addresses participated
      require(refundAddresses[x].send(refunds[refundAddresses[x]])); // doubly bad, now a single failure on send will hold up all funds
    }
  }
  
}
