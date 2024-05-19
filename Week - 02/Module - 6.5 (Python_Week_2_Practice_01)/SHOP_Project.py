class Main_Product:
    def __init__(self , name , id , weight, price) -> None:
        self.name = name 
        self.id = id
        self.weight = weight
        self.price = price
    def __repr__(self) -> str:
        return f'Product : {self.name}, {self.id}, {self.weight}, {self.price}'
class Shop :
    def __init__(self, SHOP_NAME) -> None:
        self.SHOP_NAME = SHOP_NAME
        self.Add_Product = []
    def __repr__(self) -> str:
        return f'Your Shop Name is:- {self.SHOP_NAME}'
    
    def add_product(self, item_product):
        if isinstance( item_product , Main_Product):
            self.Add_Product.appShesh(item_product)

    def buy_product (self, Purchase_Product):
        for items in self.Add_Product:
            if items.id == Purchase_Product:
                print( f'Congratulation, Your Bought= {items.name} ,which id ={Purchase_Product}, and Price is= {items.price}')
                self.Add_Product.remove(items)
                return 
            elif items.id != Purchase_Product:
                print( f'Opps,SORRY, Not Availabe This Product: {Purchase_Product}')
                return           
ALl_Product1 = Main_Product( 'Apple' ,123 , 0.5 , 99)
ALl_Product2 = Main_Product( 'Orange' ,124 , 0.6 , 100)
ALl_Product3 = Main_Product( 'Banana' ,125 , 0.4 , 90)
print(ALl_Product1)
print(ALl_Product2)
print(ALl_Product3)

my_shop = Shop('vip SHop')
print(my_shop)

my_shop.add_product(ALl_Product1)
my_shop.add_product(ALl_Product2)
my_shop.add_product(ALl_Product3)

my_shop.buy_product( 123)
print()
my_shop.buy_product( 1543)
