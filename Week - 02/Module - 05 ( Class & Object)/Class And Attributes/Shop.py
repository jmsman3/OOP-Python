class shop():
    cart = [] #Here cart is a class attribute

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart( self , item):
        self.cart.append(item)

mehzabeen = shop('Meh za been')
mehzabeen.add_to_cart('Shoes')
mehzabeen.add_to_cart('Phone')
print( mehzabeen.cart)

nishoo = shop('Nis hoo')
nishoo.add_to_cart( 'Cap')
nishoo.add_to_cart('watch')
print(nishoo.cart)
