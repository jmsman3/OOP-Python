# # from abc import ABC , abstractmethod

# class Abstract_Properties:
#     def __init__(self,email,password ) -> None:
#         self.email = email 
#         self.password = password
        

# class Shop_App(Abstract_Properties):
#      pass

#___________________________________________________________________________________
#___________________________________________________________________________________
from Seller import Seller_Features ,add_Product_process
from Customer_Order_place import Customer_Ordering

class Shop_Features:
    def __init__(self, name):
        self.name = name 
        self.customers= {}
        self.emails = []
        self.passwords = []
        #{12: name_object}
    
    def Register(self,name, email, password):
        self.name = name 
        self.emails.append(email)
        self.passwords.append(password)
        self.customers[email] = name 
        print(f" {name}Account Register done Under this mail:- {email}")

    def login (self,email , password):
        if email not in self.emails and password in self.passwords:
            print(f"Hey,Your E-mail Wrong.But Password: {password} is Correct...!")

        elif email  in self.emails and password not in self.passwords:
            print(f"Hey,Your Password Wrong. But Email {email} is Correct...!")

        elif email in self.emails and password in self.passwords:
            print(f'Congratulations,login Successful ')
            print("=========Welcome in our Shop=========")

        else:
            print("E-mail , Password Both Wrong")


    def show_customers_list(self):
        for custmers,name in self.customers.items():
            print("mail\t\tname")
            print(f"{custmers}\t\t{name}")


#___________________________________________________________________________________
#___________________________________________________________________________________
sellr_featuree = Seller_Features("Awesonme Feature")
stuffs_add = add_Product_process("Best Dress",1123)
class Seller_persons:
    def __init__(self, seller_name) -> None:
          self.seller_name = seller_name

    
    def Register_Seller(self, name , email , password):
        sellr_featuree.Register(name, email, password)
    
    def Seller_login(self, email , password):
        sellr_featuree.login(email , password)
    
    def view_seller(self):
        sellr_featuree.show()
    
    def Seller_add_Product(self , name , id):
        stuffs_add.add_product(name,id)

    def Seller_Publish_product(self):
        stuffs_add.show_product()
#___________________________________________________________________________________
#___________________________________________________________________________________

order_nows = Customer_Ordering("Bismillah Shop", 456)
class take_order_from_customer:
    def __init__(self,customer_name) -> None:
        self.customer_name = customer_name

    def take_product_order(self, id): 
        self.id = id
        order_nows.order_product(id)

    



# app = Shop_Features("Mashallah_Shop")
# while True:
#     print("1. Regsiter")
#     print("2. Log in")
#     print("3. View Customers")
#     print("4. Logout")
#     ch = int(input("Enter Choice: "))
#     if ch == 1:
#         name = input("Enter Customer Name: ")
#         email = input("Enter mail: ")
#         password = input("Enter Pass: ")
#         app.Register(name, email , password)
#     elif ch == 2:
#         email = input("Enter mail: ")
#         password = input("Enter Pass: ")
#         app.login(email , password)
#     elif ch == 3:
#         app.show_customers()
#     elif ch == 4:
#         print("Logut Done....!")
#         break
#     else:
#         print("Invalid choice")




        

        






    
        