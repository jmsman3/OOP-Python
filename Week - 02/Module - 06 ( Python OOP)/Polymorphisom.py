# poly = many(multiple)
# mor = Shape
class Animal:
    def __init__(self,name) -> None:
        self.name = name 
    def make_sound(self):
        print("Animal making Some Sound")    
#------------------------------------------------------------------------
class cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("Mewo Mewo...")
#------------------------------------------------------------------------
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("Ghew Ghew")
#------------------------------------------------------------------------
class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("Behh Behh.....")
#------------------------------------------------------------------------

don = cat("real don")
don.make_sound()

shepard = Dog("Real Dogs")
shepard.make_sound()

mess = Goat("L M")
mess.make_sound()
#------------------------------------------------------------------------

# less = Goat("Gora Gori")
animals = [don, shepard, mess]
for animal in animals:
    animal.make_sound()
