from Food_item import Food_item
from user import Customer , Employee, Admin
from restaurent import Restaurent

mamar_restaurent = Restaurent("Mamar Restaurent")
def customer_menu():
    name = input("Enter your name: ")
    phone = int(input("Enter Your Phone: "))
    email = input("Enter your email: ")
    address = input("Enter Your address: ")
    customar = Customer(name= name , phone= phone, email= email , address= address)
    
    while True:
        print(f"welcome {customar.name}..!!")
        print("1. View menu: ")
        print("2. Add item to Cart: ")
        print("3. View Cart: ")
        print("4. Pay Bill: ")
        print("5. Exit: ")

        choice = int(input("Enter Your choice: "))
        if choice ==1:
            customar.view_menu(mamar_restaurent)
        elif choice == 2:
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            customar.add_to_cart(mamar_restaurent, item_name, quantity)
        elif choice ==3:
            customar.view_cart()
        elif choice ==4:
            customar.pay_bil()
        elif choice ==5:
            print("Exit Done..!")
            break
        else:
            print("Invalid Number")

def Admin_menu():
    name = input("Enter Your Name:")
    email = input("Enter Your Email:")
    phone = int(input("Enter Your phone:"))
    address = input("Enter Your address:")
    admin = Admin(name= name, email=email, phone=phone, address= address)

    while True:
        print(f"Welcome {admin.name}...!!")
        print("1.Add new item: ")
        print("2.Add new Employee: ")
        print("3.View Employee: ")
        print("4.View Items: ")
        print("5.Delete items: ")
        print("6.Exit: ")

        choice = int(input("Enter your choice: "))

        if choice ==1:
            item_name = input("Enter Item name: ")
            item_price = int(input("Enter Item Price: "))
            itm_quantity = int(input("Enter Item Quantity:"))

            item = Food_item(item_name,item_price, itm_quantity)
            admin.add_new_item(mamar_restaurent, item)

        elif choice ==2:
             name = input("Enter employee name: ")
             phone = input("Enter employee phone: ")
             email = input("Enter employee email: ")
             address = input("Enter employee address: ")
             age = input("Enter employee age: ")
             designation = input("Enter employee designation: ")
             salary = input("Enter employee salary: ")
             employee = Employee(name, phone, email,address,age,designation,salary)
             admin.add_employee(mamar_restaurent , employee)

        elif choice == 3:
            admin.view_employee(mamar_restaurent)

        elif choice ==4:
            admin.view_menu(mamar_restaurent)

        elif choice ==5:
            item_name = input("Enter item name: ")
            admin.remove_item(mamar_restaurent,item_name)

        elif choice ==6:
            break 
        else:
            print("Invalid Number")

while True:
    print("Welcom TO OUR Restaurent...!")
    print("1.Customer")
    print("2.Admin")
    print("3.Exit")

    choice = int(input("Enter Your choice: "))
    if choice == 1:
        customer_menu()
    elif choice ==2:
        Admin_menu()
    elif choice == 3:
        break 
    else:
        print("Invalid Input...!")
            
        
             
    

       