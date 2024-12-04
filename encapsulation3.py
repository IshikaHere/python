class bank a/c:
  __bal #private attribute

  get_bal(): #public
  deposit(self,amt):  #public
  if amt>0:
    self.__bal += amt
    print(bal)
  else:
      print(deposit amt should be greater than zero)

   withdraw(self,amt):  #public
   if 0<amt<=self.__bal:
    self.__bal -= amt
    print(bal)
   else:
      print(insufficent amt)

      account = bank_account("neha",500)
      account deposit(400)
