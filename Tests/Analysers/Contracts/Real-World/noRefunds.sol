pragma solidity ^0.4.19;

/*
*
* Authio WarGame - level 03: "NoRefunds"
*
* Objectives:
*   1. Steal the contract's 'token' balance (Set your balance to 10000)
*
*/
contract NoRefunds {

  //Amount the owner can withdraw
  uint public withdraw_amount = 0;
  //Address to which the owner will withdraw
  address public withdraw_beneficiary = address(0);

  //Owner - can update withdraw amount and beneficiary
  address public owner;

  //Allows a user to request a refund of tokens, which can be approved by the owner
  struct RefundReq {
    uint request_amount;
    address request_beneficiary;
    bool approved;
  }

  //Maps addresses to refund requests
  mapping (address => RefundReq) public pending_refunds;
  //Maps addresses to uint balances
  mapping (address => uint) public balances;

  //Modifier - sender must be the contract owner
  modifier onlyOwner() {
    require(msg.sender == owner);
    _;
  }

  //Constructor: Set sender as owner and give the contract an initial balance of 10000
  function NoRefunds() public {
    owner = msg.sender;
    balances[address(this)] = 10000;
  }

  //Allows the owner to set a beneficiary to withdraw to
  function setBeneficiary(address _beneficiary) public onlyOwner() {
    require(withdraw_beneficiary == address(0));
    withdraw_beneficiary = _beneficiary;
  }

  //Allows the owner to set the amount to withdraw to a beneficiary
  function setWithdrawAmount(uint _amount) public onlyOwner() {
    require(withdraw_amount == 0);
    withdraw_amount = _amount;
  }

  //Allows the owner to approve refunds requested by users
  function approveRefund(address _requestor) public onlyOwner() {
    pending_refunds[_requestor].approved = true;
  }

  //Once a beneficiary and amount has been set by the owner, anyone can withdraw those tokens to the beneficiary
  function withdrawBalance() public {
    require(withdraw_beneficiary != address(0));
    giveTokens(withdraw_beneficiary, withdraw_amount);
  }

  //Allows a user to request a refund. If the signify that the refund is to be activated,
  //then the beneficiary will be given the refund (if the owner has already approved the request)
  function refund(bool _activate_refund, uint _amount, address _beneficiary) public {
    if (_activate_refund) {
      RefundReq storage req = pending_refunds[msg.sender];
      require(req.approved);
      require(req.request_amount <= _amount);
      require(req.request_beneficiary == _beneficiary);
      req.approved = false;
      giveTokens(_beneficiary, _amount);
    } else {
      req.request_amount = _amount;
      req.request_beneficiary = _beneficiary;
      req.approved = false;
    }
  }

  //Private function - used to distribute tokens to an address from the contract's balance
  function giveTokens(address _to, uint _amount) private {
    require(balances[address(this)] >= _amount);
    balances[address(this)] -= _amount;
    balances[_to] += _amount;
  }

}
