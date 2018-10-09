contract UncheckedPatterns {

  address callee = 0xE0F7e56e62b4267062172495D7506087205A4229;

  function callCheckedWithAssert()  {
    assert(callee.call());
  }

  function callCheckedWithIf()  {
    if(callee.call() == false) {
      revert();
    }
    if(!callee.call()) {
      revert();
    }
  }

  function uncheckedCall()  {
      callee.call();
  }

}
