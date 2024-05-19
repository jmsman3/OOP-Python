import random
class User:
    def __init__(self,name,email ,address , account_type):
        self.name = name
        self.address = address 
        self.email = email 
        self.account_type = account_type 
        self.account_number = random.randint(1000000,9999999)
        self.transation_history = []
        self.loan_count = 0
        self.balance = 0
        self.loan_balance = 0
    
    def deposit(self, amount):
        self.balance += amount 
        self.transation_history.append(f"Last Deposited: +{amount} Taka/=")
        print(f"Deposite Done {amount} Taka/= To account Number {self.account_number}\nNew Balance:= {self.balance} taka/=")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transation_history.append(f"Last Withdraw: -{amount} Taka/=")
            print(f"Withdraw Done {amount} Taka/= To account Number {self.account_number}\nNew Balance:= {self.balance} taka/=")


    def Check_balance(self):
        print(f"Current Balance: {self.balance}")
        return self.balance
    

    def Check_transation_history(self):
        for transation in self.transation_history:
            print(transation)
        return self.transation_history
    
    def take_loan(self,amount):
        if self.loan_count >=2:
            print("Sorry,Loan Limit Shesh...!")
        else:
            self.balance += amount 
            self.loan_balance += amount 
            self.loan_count += 1
            self.transation_history.append(f"Last Loan taken: {amount}")
            print(f"Loan You got: {amount} taka/=\nNew Balance Now: {self.balance}")
    
    def Transfer(self, amount, receipent_account):
        if amount >self.balance:
            print("Sorry, You Do not have Sufficient Balance For transfer...!!")
        else:
            self.balance -= amount 
            receipent_account.balance += amount 
            self.transation_history.append(f"Send {amount} taka/= to Account Number: {receipent_account.account_number}")
            receipent_account.transation_history.append(f"Received {amount} taka/= from {self.account_number}")
            print(f"Tranfer {amount} taka/= to {receipent_account.account_number}\nNew Balance: {self.balance}")


#_______________________________________________________====(Admin Site)======________________________________________________________________________________________________________________
 #===========================================================================================================================


class Admin:
    def __init__(self):
        self.users ={}
        self.loan_features = True

    def create_account(self,name,email ,address , account_type ):
        user = User(name,email,address, account_type)
        self.users[user.account_number] = user  #account number aikhane key() and user holo values
        print(f"Successfully Account created....!\t\n Account name: {name}\nAccount Number: {user.account_number}")
    
    def find_users(self,account_number):
        for user in self.users.values():
            if user.account_number == account_number:
                return user
        print("Wrong Account Number...!!!")
        return None
    
    def delete_account(self, account_number):
        if account_number in self.users:
            del self.users[account_number]
            print(f"Successfully Deleted this Account: {account_number}")
        else :
            print(f"Account Number Not Found, Please Enter Correct account number,Thank You....!")
    
    def list_account(self):
        for account_numbers , user  in self.users.items():
            print(f"Account Number: {account_numbers}\nPerson name: {user.name}\n{user.name}'s Balnace: {user.balance}\n{user.name}'s Account Type: {user.account_type}\n")
    
    # total_MOney =0
    def Total_Balance(self):
        total =sum(user.balance for user in self.users.values()) 
        print(f"Totla Balance in The Bank: {total}")
        return total 
       
    # total_LOAN_Money =0 
    def total_loan_amount(self):
        Total_Loan = sum(user.loan_balance for user in self.users.values() )
        print(f"Total Bank Loan/dhar/dena Amount is : {Total_Loan}")
        return Total_Loan 
    
    def Loan_feature_Open_close(self,input_Decision):
        if input_Decision == 1:
            self.loan_features = True 
            feature_condition = "ON"
        elif input_Decision == 0:
            self.loan_features = False
            feature_condition = "OFF"
        print(f"Opps...!!, Sorry, Loan Featured Turned: {feature_condition}....!!")

# def Bank_Final_System_process():
admin = Admin()
while True:
    print("\n=====Welcome To Bank Management System=====")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    choice = int(input("Enter Choice: "))
    if choice == 1:
        while True:
            print("====Welcom To Admin Dash Board====")
            print("\n")
            print("1.Create Account: ")
            print("2.Delete Account: ")
            print("3.View All Account List: ")
            print("4.Check Total BalanceL: ")
            print("5.Check Loan Total Balance: ")
            print("6.Turn ON/OFF loan Feature: ")
            print("7.Exit")

            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                name = input("Enter Your Name: ")
                email = input("Enter E-mail: ")
                address = input("Enter Address: ")
                acc_type = input("Account Type(Current/Savings): ")
                admin.create_account(name = name , email= email , address= address , account_type= acc_type)
            elif choice == 2:
                account_number = int(input("Enter The Account number which You wanna Delet: "))
                admin.delete_account(account_number)
            elif choice == 3:
                admin.list_account()
            elif choice == 4:
                admin.Total_Balance()
            elif choice == 5:
                admin.total_loan_amount()
            elif choice == 6:
                Seddhanto = int(input("Turn on or Off Enter 0/1: "))
                admin.Loan_feature_Open_close(input_Decision=Seddhanto)

            elif choice == 7:
                print("Exit SucessFully Done........!")
                break
            else:
                print("Invalid Admin Choice: ")
    
    elif choice == 2:
        Enter_acc_number = int(input("Enter USer Account Number: \n"))
        print()
        user = admin.find_users(Enter_acc_number)
        if user:
            while True:
                
                # user = User()
                print("=========Welcome to User Dashboard========")
                print("1. Deposit Amount")
                print("2. Withdraw Amount")
                print("3. Check Balance")
                print("4. Check Transaction History")
                print("5. Take Loan")
                print("6. Transfer Amount")
                print("7. Exit")

                choice = int(input("Enter your Choice: "))
                if choice == 1:
                    deposit_amount = int(input("Enter Your Deposite Amount: "))
                    user.deposit(deposit_amount)
                    
                elif choice == 2:
                    with_drwaAmount = int(input("Enter withdrwa Amount: "))
                    user.withdraw(with_drwaAmount)
                elif choice == 3:
                    user.Check_balance()
                elif choice == 4:
                    user.Check_transation_history()

                elif choice ==5:
                    loan_neba = int(input("Enter Need-Load Amount: "))
                    if admin.loan_features:
                        user.take_loan(loan_neba)
                    else:
                        print("Loan Feature is Turned OFF...!!")

                elif choice == 6:
                    Transferable_amount = int(input("Enter Transferable_amount Amount: "))
                    receipent_acc_number = int(input("Enter Receiver Account Number: "))
                    recivar = admin.find_users(receipent_acc_number)
                    if recivar :
                        user.Transfer(Transferable_amount , recivar)
                    else:
                        print("OPPS!!!, Sorry...Wrogn Account Number...!")
                elif choice == 7:
                    print("User Exit DOne.........!")
                    break 
                else:
                    print("Wrong user Choice...!")
        else:
            print("Account not found...!")
    elif choice == 3:
        print("FUll Logout The Bank Sytem...TATA Good Bye....!!!")
        break 
    else :
        print("Invalid Choic Number...!")
        



                
                    



        
        





        

            




