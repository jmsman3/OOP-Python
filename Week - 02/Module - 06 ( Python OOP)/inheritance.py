#base class, common class, common attribute + functionaluity class
# derived class , child class, uncommon attribute + functionality class

class Gadget:
    def __init__(self, brand , price , color , origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin 
        
    def run(self):
        return f'Running Laptop :{self.brand}'
    
#-----------------------------------------------------------------------------
class Laptop:
    def __init__(self, memory,ssd) -> None:
        self.ssd = ssd
        self.memory = memory
    def coding( self):
        return f'learning python and practising'
#-----------------------------------------------------------------------------
class phone(Gadget):
    def __init__(self,brand , price , color, origin,dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def phone_cal(self, number , text):
        return f'Sending Sms :{number} with : {text}'
    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.origin} {self.color} { self.price} {self.dual_sim}'
#-----------------------------------------------------------------------------
class camera :
    def __init__(self, pixel) -> None:
        self.pixel = pixel
    def change_lens(self):
        pass
#-----------------------------------------------------------------------------
my_phone = phone('iphone', 120000, 'Silver', 'china', True)
# my_phone.phone_cal()
print(my_phone.brand)
print( my_phone)
    