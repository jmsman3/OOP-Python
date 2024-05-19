#encapsulation.py
# 3 types:- Public , Protected, private
class Bank:
    def __init__(self , holder_name , initial_deposite) -> None:
        self.holder_name = holder_name
        self._branch = 'banani 11'
        self.__Balance = initial_deposite
#-------------------------------------------------------------------------
    def deposite( self, amount):
        self.__Balance += amount
        print(f'Successfully Deposite := {self.__Balance}')
#--------------------------------------------------------------------------
    def get_balance(self):
        return  f'Now Your Balance := {self.__Balance}'
    
#---------------------------------------------------------------------------
    def withdraw(self, amount):
        if amount < self.__Balance:
            self.__Balance -= amount
            return print(f'bahir Korso := {amount}')
        else:
            print(f'Fokira taka nai')

rafsan = Bank('Choto Bhai' , 10000)
print( rafsan.holder_name , rafsan._branch)
rafsan.deposite(5000)
rafsan.withdraw(3000)
print(dir(rafsan))#Privare Access kore "dir" deye

print(f'check please:- {rafsan._Bank__Balance}')
print( rafsan.get_balance())




        