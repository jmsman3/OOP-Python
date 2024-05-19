from abc import ABC , abstractmethod
class Animal(ABC):
    def eat(self):
        print('i need food')
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.catagory = 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print('hey na nana !, i am eating banana')
    def move (self):
        print('Hanging on the brances')

lyka  = Monkey('Lucky')
lyka.eat()