class Book:
    def __init__(self,name) -> None:
        self.name= name
    def read(self):
        raise NotImplemented
class Pyhsics(Book):
    def __init__(self, name,lab) -> None:
        self.lab = lab
        super().__init__(name)
    def read(self):
        print("I am reading topon Sir Book")
topon = Pyhsics('topon' , True)
print(issubclass( Pyhsics , Book))
print(isinstance( topon , Pyhsics))
print(isinstance(topon , Book))

topon.read()