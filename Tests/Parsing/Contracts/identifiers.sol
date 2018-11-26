pragma solidity ^0.4.24;

contract TestTypes {

  address typeAddr;
  bool typeBool = true;
  string typeString;
  int typeInt;
  uint typeUint;
  byte typeByte;
  
  mapping (address => uint) typeMapping;
  uint[10] typeArray;
  struct TypeStruct {
    uint typeStruct_uint;
    string typeStruct_string;
  }

  TypeStruct typeStruct;
  
  function foo () {
    int local_typeInt;
    
    typeAddr = msg.sender;
    typeBool = false;
    typeString = "hello world";
    typeInt = -10;
    typeUint = 10;
    typeByte = "a";

    typeMapping[msg.sender] = 100;
    typeArray[0] = 10;
    typeStruct.typeStruct_uint = 10;
    typeStruct.typeStruct_string = "hello string";

    local_typeInt = typeInt;

    string local_typeString;
    
  }
  
}
