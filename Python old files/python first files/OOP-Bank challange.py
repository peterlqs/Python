class Account():
    def __init__(self,owner,balance=0):
        self.owner= owner
        self.balance= balance
        print("Account owner:", owner)
        print("Account balance: ${}".format(balance))
    def owner():
        print(self.owner)
    def balance(self):
        print(self.balance)
    def deposit(self,a):
        self.balance += a
        print('Deposit Accepted')
    def withdraw(self,b):
        if self.balance >= b:
            print("Withdrawal Accepted")
            self.balance -= b
        else:
            print("Funds Unavailable")
acct1 = Account('Jose',100)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)