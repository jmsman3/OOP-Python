from math import pi
class shape:
    def __init__(self, name) -> None:
        self.name = name
class rectangle(shape):
    def __init__(self, name, length , weidth) -> None:
        self.length = length
        self.weidth = weidth
        super().__init__(name)
    def area(self):
        return self.length*self.weidth
class circle(shape):
    def __init__(self, name, radious) -> None:
        self.radious = radious
        super().__init__(name)
        # res = pi * self.radious *self.radious
    def cir_area(self):
        return pi * self.radious *self.radious
class Squaree(shape):
    def __init__(self, name, square_length) -> None:
        self.square_length = square_length
        super().__init__(name)
    def sq_area(self):
        return self.square_length * self.square_length
rec = rectangle("Ayto_Khetro", 5 ,7)
print( f'Your Khetrofol : {rec.area()}')

cir= circle("Britto" , 3)
print( f"Your Khetrofol : {cir.cir_area()}")

sqr = Squaree("Borgo_Khetro", 6)
print( f"YOur Borgo holo : {sqr.sq_area()}")



