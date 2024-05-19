class Shopping:
    # cart = []        #Class Attribute
    # # Origin = 'China' 
    location = None

    def __init__(self,name , location) -> None:
        self.name = name #Instance attribut 
        Shopping.location = location

    @staticmethod
    def Sum ( a,b):
        res = a+b
        print(f'Your Summation is:-{res} ')


    @classmethod
    def Purchase(cls, item , price ,amount):
        # super().__init__(Shopping)
        print(cls.location)
        remaing = amount - price
        print(f'Buying:- {item} for Price:-{price} and Remaing :-{remaing}')
    

Basundra = Shopping( 'BasunDra_shop' , 'DHAKA')
Basundra.Purchase( 'Lungi' , 20,30 )
# print()
# # Shopping.Purchase( 'v' , 12, 18)
# #Below Static Method
# Shopping.Sum( 10,9) 
# Basundra.Sum(10,8)