from Seller import Seller_Features ,add_Product_process 
produc_Example = add_Product_process("Lungi", 1124)
class Customer_Ordering:
    def __init__(self,name_shop,id) -> None:
        self.id = id
        self.name_shop = name_shop
        
    def order_product(self,id): 
        if id not in produc_Example.product_database.values():
            print("Wrong Product id")
        else:
            if id in produc_Example.product_database.values():
                print(f"Orderplace Successfull of this: {id}")
                produc_Example.product_database.remove(id)
                


            
