from order import order
# from menu import Menu 
from abc import ABC 
class user:
    def __init__(self,name,phone,email,address):
        self.name = name 
        self.phone = phone
        self.email = email
        self.address = address
#---------------------------------------------------------
#----------------------------------------------------------------------
class Customer(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = order()
    
    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item is not None :
            if quantity > item.quantity:
                print("item quantity Exceeded")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("item added")
        else:
            print("item not found")


    def view_cart(self):
        print("view cart....!!")
        print("Name\tPrice\tQuantity")
        for item , quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"total price: {self.cart.total_price}")
    
    def pay_bil(self):
        print(f"total {self.cart.total_price} paid Successfully")
        self.cart.clear()
             

class Employee(user):
    def __init__(self, name, phone, email, address,age,designation,salary):
        self.age = age
        self.designation = designation
        self.salary = salary
        super().__init__(name, phone, email, address)

class Admin(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def add_employee(self, restaurent , employee):
        restaurent.add_employee(employee)
    
    def view_employee(self, restaurent):
        restaurent.view_employee()
    
    def add_new_item(self, restaurent, item):
        restaurent.menu.add_new_item(item)
    
    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
