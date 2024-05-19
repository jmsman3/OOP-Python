class Laptop:
    def __init__(self, brand , price , color , memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
    def run(self):
        return f'Running Laptop :{self.brand}'
    def coding( self):
        return f'learning python and practising'
class phone:
    def __init__(self,brand , price , color, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim
    def run(self):
        return f'Phone tipa tipi kore'
    def phone_cal(self, number , text):
        return f'Sending Sms :{number} with : {text}'
class camera :
    def __init__(self,brand , price , color, pixel) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel
    def run(self):
        pass
    def change_lens(self):
        pass


    