// From https://consensys.github.io/smart-contract-best-practices/known_attacks/#reentrancy
// INSECURE
contract Reentrancy {
  mapping (address => uint) private userBalances;
  
  function withdrawBalance() public {
    uint amountToWithdraw = userBalances[msg.sender];
    require(msg.sender.call.value(amountToWithdraw)()); // At this point, the caller's code is executed, and can call withdrawBalance again
    userBalances[msg.sender] = 0;
  }

  function withdrawBalanceSafer() public {
    uint amountToWithdraw = userBalances[msg.sender];
    userBalances[msg.sender] = 0;
    require(msg.sender.call.value(amountToWithdraw)()); // The user's balance is already 0, so future invocations won't withdraw anything
  }
    
  function withdrawBalanceLocalMod() public {
    uint amountToWithdraw = userBalances[msg.sender];
    uint local_count;
    userBalances[msg.sender] = 0;
    require(msg.sender.call.value(amountToWithdraw)());
    amountToWithdraw = 0;
  }

}
