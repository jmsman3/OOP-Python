from abc import ABC 
class user:
    def __init__(self,name,phone,email,address):
        self.name = name 
        self.phone = phone
        self.email = email
        self.address = address
#---------------------------------------------------------
class Restaurent:
    def __init__(self,name):
        self.name = name
        self.employees = []
        self.menu= Menu()

    def add_employee(self,Employee):
        self.employees.append(Employee)

    def view_employee(self):
        print("|=================(Employee List)=================|")
        for emp in self.employees:
            print("(name)\t\t(email)\t\t(phone)\t(address)")
            print(emp.name, "\t", emp.email,"\t",emp.phone,"\t",emp.address)
#----------------------------------------------------------------------
class Customer(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = order()
    
    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item is not None:
            if quantity > item.quantity:
                print("item quantity Exceeded")
            else:
                item.quantity == quantity
                self.cart.add_item(item)
                print("item added")
        else:
            print("item not found")


    def view_cart(self):
        print("view cart....!!")
        print("Name\tPrice\tQuantity")
        for item , quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{item.quantity}")
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
    
    def view_item(self, restaurent):
        restaurent.menu.show_menu()
    



class Menu:
    def __init__(self):
        self.items = [] #items er database

    def add_new_item(self, item):
        self.items.append(item)
    
    def find_item(self,item_name): # find_item function ta banano hoise remove item bananor jonno
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None 
    
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item is not None: #Shudhu if item: airokom likhle o hoi
            self.items.remove(item)
            print("item deleted")
        else:
            print("Item Not Found")
    
    def show_menu(self):
        print("=====Menu=====")
        print("Name\tPrice\tQuantity")
        for item in self.items :
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class Food_item:
    def __init__(self, name , price , quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity 

    

    
class order:
    def __init__(self) -> None:
        self.items= {}
    
    def add_item(self, item):
        if item in self.items: # jodi item ta cart e thake
            self.items[item] += item.quantity
        else:  
            self.items[item] = item.quantity #item cart e jodi na thake

    def remove(self, item):
        if item is self.items:
            del self.items[item]
    
    def total_price(self):
        return sum(item.price * quantity for item , quantity in self.items.items())
    
    def clear(self):
        self.items = {}
    

