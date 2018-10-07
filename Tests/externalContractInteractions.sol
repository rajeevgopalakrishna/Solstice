contract ExternalContractInteractions {

  address callee = 0xE0F7e56e62b4267062172495D7506087205A4229;

  function foo ()  {
      	callee.transfer(1);
  	callee.send(1);
	callee.call();
	callee.delegatecall();
  }

}
