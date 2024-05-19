from Seller import Seller_Features ,add_Product_process
from Customer_Order_place import Customer_Ordering
from Shopping_App import Shop_Features ,Seller_persons, take_order_from_customer

My_shop = Shop_Features("MashAllah_Shop")
Sell_Boy = Seller_persons("Rahim Mia")
Human = take_order_from_customer("Nice Manus")
#------------------------------------------------------------------------------------
def method_seller():
    while True :
        print("===Welcome to Seller DashBoard")
        print("1.Seller Registration: ")
        print("2.Seller Log-in")
        print("3.Add Product by Seller: ")
        print("4.Log-Out Seller")
        
        ch = int(input("Enter Choice: "))
        if ch == 1:
            name = input("Enter name: ")
            email = input("Enter Email: ")
            password = input("Enter password: ")
            Sell_Boy.Register_Seller(name, email, password)

        elif ch == 2:
            email = input("Enter Email: ")
            password = input("Enter password: ")
            Sell_Boy.Seller_login( email, password)
        elif ch == 3:
             name = input("Enter name: ")
             id = int(input("Enter Product id: "))
             Sell_Boy.Seller_add_Product(name, id)
        elif ch == 4:
            print("Log-Out Successfull of Seller")
            break 
        else :
            print("invalid Choice")
        print()
#-----------------------------------------------------------------------------------------------------------------
def method_of_customer():

    while True:
        print("===Welcome to **CUSTOMER** DashBoard")
        print("1.Customer Registration: ")
        print("2.Customer Log-in: ")
        print("3.View All Product: ")
        print("4.Order your Product: ")
        print("5.Log-Out Customer: ")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            name = input("Enter name: ")
            email = input("Enter Email: ")
            password = input("Enter password: ")
            My_shop.Register(name, email, password)
        elif ch == 2:
            email = input("Enter Email: ")
            password = input("Enter password: ")
            My_shop.login(email, password)
          
        elif ch == 3:
            Sell_Boy.Seller_Publish_product()
        elif ch == 4:
            id = int(input("Enter Product id: "))
            Human.take_product_order(id)

        elif ch == 5:
            print("Log-Out Successfull of Customer")
            break
        else :
            print("invalid Choice")
#---------------------------------------------------------------------------------------------------------------------------------

while True:
        
    print("1. Company CEO")
    print("2.Seller")
    print("3.Customer")
    print("4.Exit")

    ch = int(input("Enter Choice: "))
    if ch == 1:
        Sell_Boy.view_seller()
    elif ch == 2:
        method_seller()
    elif ch == 3:
        method_of_customer()
    elif ch == 4:
        print("Exit Successfull")
        break 
    else:
        print("Invalid Choice")
    





