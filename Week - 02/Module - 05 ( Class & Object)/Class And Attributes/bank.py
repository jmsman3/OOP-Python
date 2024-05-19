class Bank :
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
    
    def get_balance(self):
        return self.balance
    
    def deposit( self, amount):
        if amount >0:
            self.balance += amount
            # print( f'Your Deposit Final Balance = {self.get_balance()}')
    
    def withdraw( self, amount):
        if amount <self.min_withdraw:
            print( f'fakira .CanNot withdraw below ={self.min_withdraw}')
        elif amount > self.max_withdraw:
            print( f'Bank Will Gorib. Cannot withdrw more than ={self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'here is your money {amount}')
            print( f'Your Balance After WithDraw {self.get_balance()}')

# brac = Bank(15000)
# brac.withdraw(50)
# brac.withdraw(500000000000)
# brac.withdraw(1000)

Dbbl = Bank(5000)
Dbbl.deposit(2000)
Dbbl.deposit(2000)
print(Dbbl.get_balance())









        














































