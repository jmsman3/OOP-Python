class shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
    
    def add_to_cart( self, item, price, quantity):
        product = {'item':item ,'price':price,'quantity':quantity}
        self.cart.append(product)
 
    def Check_Out( self, amount):
        totall = 0
        for item in self.cart:
            # print( item)
            totall += item['price']  * item['quantity']
        print( 'total price' , totall)
        if amount < totall:
            print( f'Please Provide {totall - amount} more')
        else :
            extra = amount - totall
            print(f'here is your items and Extra Money: {extra}')
    
      #HomeWork
    # def remove_item(self, item):
    #     total = 0
    #     for itm in self.cart:
    #         total -= itm['price']*itm['quantity']
    #     print( 'Remove Item', total)

swapon = shopping('Alan Swapon')
swapon.add_to_cart('alu', 50,6)
swapon.add_to_cart('dim', 12,24)
swapon.add_to_cart('rice', 50,5)

print(swapon.cart)
# swapon.Check_Out(600)
swapon.Check_Out(1000)
# swapon.remove_item(200)
        
        