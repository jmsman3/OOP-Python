# import random

# class User:
#     def __init__(self, name, email, address, account_type):
#         self.name = name
#         self.email = email
#         self.address = address
#         self.account_type = account_type
#         self.balance = 0
#         self.account_number = self.generate_account_number()
#         self.transaction_history = []
#         self.loan_count = 0

#     def generate_account_number(self):
#         return random.randint(1000000000, 9999999999)

#     def deposit(self, amount):
#         self.balance += amount
#         self.transaction_history.append(f"Deposited {amount}")
#         print(f"Deposited {amount} successfully.")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Withdrawal amount exceeded")
#         else:
#             self.balance -= amount
#             self.transaction_history.append(f"Withdrew {amount}")
#             print(f"Withdrew {amount} successfully.")

#     def check_balance(self):
#         print(f"Available balance: {self.balance}")
#         return self.balance

#     def check_transaction_history(self):
#         print("Transaction history:")
#         for transaction in self.transaction_history:
#             print(transaction)
#         return self.transaction_history

#     def take_loan(self):
#         if self.loan_count < 2:
#             self.loan_count += 1
#             print("Loan approved.")
#             return True
#         else:
#             print("Loan limit reached.")
#             return False

#     def transfer(self, amount, recipient):
#         if self.balance >= amount:
#             self.balance -= amount
#             recipient.balance += amount
#             self.transaction_history.append(f"Transferred {amount} to {recipient.name}")
#             print(f"Transferred {amount} to {recipient.name} successfully.")
#         else:
#             print("Insufficient funds to transfer")

# class Admin:
#     def __init__(self):
#         self.users = []
#         self.loan_feature = True

#     def create_account(self, name, email, address, account_type):
#         user = User(name, email, address, account_type)
#         self.users.append(user)
#         print(f"Account created successfully for {name} with account number {user.account_number}.")
#         return user

#     def delete_account(self, account_number):
#         user = self.find_user(account_number)
#         if user:
#             self.users.remove(user)
#             print(f"Account {account_number} deleted successfully.")
#         else:
#             print("Account not found.")

#     def find_user(self, account_number):
#         for user in self.users:
#             # if user.account_number == account_number:
#                 return user
#         return None

#     def list_all_accounts(self):
#         print("All user accounts:")
#         for user in self.users:
#             print(f"Account Number: {user.account_number}, Name: {user.name}, Email: {user.email}, Balance: {user.balance}")
#         return self.users

#     def check_total_balance(self):
#         total_balance = sum(user.balance for user in self.users)
#         print(f"Total available balance in the bank: {total_balance}")
#         return total_balance

#     def check_total_loan_amount(self):
#         total_loan_amount = sum(user.balance for user in self.users if user.loan_count > 0)
#         print(f"Total loan amount: {total_loan_amount}")
#         return total_loan_amount

#     def toggle_loan_feature(self, status):
#         self.loan_feature = status
#         state = "on" if status else "off"
#         print(f"Loan feature turned {state}.")

# def banking_system():
#     admin = Admin()
#     while True:
#         print("\nWelcome to the Banking Management System")
#         print("1. Admin Login")
#         print("2. User Login")
#         print("3. Exit")
#         choice = int(input("Enter your choice: "))
        
#         if choice == 1:
#             while True:
#                 print("\nAdmin Menu")
#                 print("1. Create Account")
#                 print("2. Delete Account")
#                 print("3. List All Accounts")
#                 print("4. Check Total Balance")
#                 print("5. Check Total Loan Amount")
#                 print("6. Toggle Loan Feature")
#                 print("7. Logout")
#                 admin_choice = int(input("Enter your choice: "))
                
#                 if admin_choice == 1:
#                     name = input("Enter name: ")
#                     email = input("Enter email: ")
#                     address = input("Enter address: ")
#                     account_type = input("Enter account type (Savings/Current): ")
#                     admin.create_account(name, email, address, account_type)
                
#                 elif admin_choice == 2:
#                     account_number = int(input("Enter account number to delete: "))
#                     admin.delete_account(account_number)
                
#                 elif admin_choice == 3:
#                     admin.list_all_accounts()
                
#                 elif admin_choice == 4:
#                     admin.check_total_balance()
                
#                 elif admin_choice == 5:
#                     admin.check_total_loan_amount()
                
#                 elif admin_choice == 6:
#                     status = input("Enter 'on' to enable loans or 'off' to disable loans: ").strip().lower() == 'on'
#                     admin.toggle_loan_feature(status)
                
#                 elif admin_choice == 7:
#                     break
                
#                 else:
#                     print("Invalid choice. Please try again.")
        
#         elif choice == 2:
#             account_number = int(input("Enter your account number: "))
#             user = admin.find_user(account_number)
#             if user:
#                 while True:
#                     print("\nUser Menu")
#                     print("1. Deposit Amount")
#                     print("2. Withdraw Amount")
#                     print("3. Check Balance")
#                     print("4. Check Transaction History")
#                     print("5. Take Loan")
#                     print("6. Transfer Amount")
#                     print("7. Logout")
#                     user_choice = int(input("Enter your choice: "))
                    
#                     if user_choice == 1:
#                         amount = float(input("Enter amount to deposit: "))
#                         user.deposit(amount)
                    
#                     elif user_choice == 2:
#                         amount = float(input("Enter amount to withdraw: "))
#                         user.withdraw(amount)
                    
#                     elif user_choice == 3:
#                         user.check_balance()
                    
#                     elif user_choice == 4:
#                         user.check_transaction_history()
                    
#                     elif user_choice == 5:
#                         if admin.loan_feature:
#                             user.take_loan()
#                         else:
#                             print("Loan feature is currently disabled.")
                    
#                     elif user_choice == 6:
#                         recipient_account_number = int(input("Enter recipient account number: "))
#                         amount = float(input("Enter amount to transfer: "))
#                         recipient = admin.find_user(recipient_account_number)
#                         if recipient:
#                             user.transfer(amount, recipient)
#                         else:
#                             print("Recipient account does not exist.")
                    
#                     elif user_choice == 7:
#                         break
                    
#                     else:
#                         print("Invalid choice. Please try again.")
#             else:
#                 print("Account not found.")
        
#         elif choice == 3:
#             print("Exiting the system. Goodbye!")
#             break
        
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     banking_system()
