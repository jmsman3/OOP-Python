class pen:
    Banglai_Bole = 'Kolom'

    def __init__(self, owner ,brand, price ,color):
        self.owner = owner
        self.brand = brand
        self.price = price
        self.color = color
 
my_pen = pen( 'Abul' , 'matador', 5, "Red")
print(my_pen.owner , my_pen.brand , my_pen.price , my_pen.color)
your_pen = pen( 'Babul' , 'Mata_Glory' , 6, 'white')
print( your_pen.owner , your_pen.brand , your_pen.price , your_pen.color)
our_pen = pen( 'Cabul', 'Pin_Point' , 7 , 'Pink')
print( our_pen.owner , our_pen.brand , our_pen.price , our_pen.color)
their_pen = pen( 'Dabul' , 'Matador_all_time' , 11, 'Balckk')
print( their_pen.owner , their_pen.brand, their_pen.price, their_pen.color)
