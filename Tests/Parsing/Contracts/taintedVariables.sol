contract TaintedVariables {

  address owner;

  modifier onlyOwner {
    if (msg.sender == owner) {
      _;
    }
  }
  
  constructor() {
    owner = msg.sender;
  }

  function foo(address addr) {
    owner = addr;
  }

  function kill() onlyOwner {
    selfdestruct(owner);
  }
  
}
