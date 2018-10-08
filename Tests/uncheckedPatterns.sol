contract UncheckedPatterns {

  address callee = 0xE0F7e56e62b4267062172495D7506087205A4229;

  function checkedCall ()  {
    assert(callee.call());
  }

  function uncheckedCall ()  {
      callee.call();
  }

}
