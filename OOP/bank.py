class BankAcount:
    def __init__(self, balance):
        self._balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance can not be negative")
        self._balance = new_balance
acount = BankAcount(1000)
acount.balance = -500
print(acount.balance)