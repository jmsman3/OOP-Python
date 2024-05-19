class shop():
    shopping_mall = 'Jamuna'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  #NOW cart is an instance Attribute
    def add_to_cart(self , item):
        self.cart.append(item)
mehjabeen = shop('Meh za been')
mehjabeen.add_to_cart('Shoe')
mehjabeen.add_to_cart('Phone')
print( mehjabeen.cart)

nishoo = shop('Nisi raat er niso')
nishoo.add_to_cart('hat')
nishoo.add_to_cart('watch')
print( nishoo.cart)

apurvoo = shop('Age Puro Silo')
apurvoo.add_to_cart('Chiriuni')
print( apurvoo.cart)