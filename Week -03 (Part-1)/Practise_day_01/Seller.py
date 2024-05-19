
class Seller_Features:
    def __init__(self, name):
        self.name = name 
        self.Sellers= {}
        self.emails = []
        self.passwords = []
        #{12: name_object}
    
    def Register(self,name, email, password):
        self.name = name 
        self.emails.append(email)
        self.passwords.append(password)
        self.Sellers[email] = password 
        print(f" {name}Account Register done Under this mail:- {email}")

    def login (self,email , password):
        if email not in self.emails and password in self.passwords:
            print(f"Hey,Your E-mail Wrong.But Password: {password} is Correct...!")

        elif email  in self.emails and password not in self.passwords:
            print(f"Hey,Your Password Wrong. But Email {email} is Correct...!")

        elif email in self.emails and password in self.passwords:
            print(f'---SEller,login Successful------')
        else:
            print("E-mail , Password Both Wrong")

    def show(self):
        for Sellers,name in self.Sellers.items():
            print("mail\t\tname")
            print(f"{Sellers}\t\t{name}")
#-------------------------------------------------------------------------------
class add_Product_process:
    def __init__(self, name,id):
        self.id = id
        self.name = name 
        self.product_database = {}
    
    def add_product(self,name,id):
        self.product_database[name] = id
    
    def show_product(self):
        for name,id in self.product_database.items():
            print("Available Product")
            print(f"name\tid")
            print(f"{name}\t{id}") 

    
        
        
    
