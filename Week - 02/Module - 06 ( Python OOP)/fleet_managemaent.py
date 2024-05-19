# Ena_Poribohon
class company:
    def __init__(self, name ,address) -> None:
        self.name = name
        self.address = address
        self.bus = []
        self.routes = []
        self.drivers = []
        self.manager = []
        self.supervisor =[]
        self.fare = []
class Driver:
    def __init__(self, name, license, age) -> None:
        self.name = name 
        self.license = license
        self.age = age
class Counter:
    def __init__(self) -> None:
        pass
    def Purchase_a_ticket ( self, start, destination):
        pass
class passenger:
    pass
class supervisor:
    pass


red_mia = Driver( 'a','123', 32) 
# print(red_mia.name)
# print(red_mia.license)
# print(red_mia.age) 
# othoba ek line e o lekha jai
print( red_mia.name , red_mia.license , red_mia.age)
