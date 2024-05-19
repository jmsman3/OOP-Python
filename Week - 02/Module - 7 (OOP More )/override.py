class Person:
    def __init__(self, name , age ,height, weight) -> None:
        self.name = name 
        self.age = age
        self.height = height 
        self.weight = weight
    def eat(self):
        print('vaat mangsho polao khabe')
    def exercise(self):
        raise NotImplementedError #aita deye baddho kora overRide Korar jonno
        
class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team  =team
        super().__init__(name, age, height, weight)
    #OverRiding
    def eat(self):
        print("Vegetables")
    def exercise(self):
        print('Gym E jaiya Poisa Khoroch')
    # + Sign Operator Over Ride
    def __add__(self,other):
        return self.age + other.age
    # * Sign Operator Over Ride
    def __mul__(self,other):
        return self.weight * other.weight
    #  Len Operator Over Ride
    def __len__(self):
        return self.height
    # > Sign Operator Over Ride
    def __gt__(self,other):
        return self.age > other.age
    

Shakib = Cricketer("Sakib" , 38,68,91,'BD')
Mushi = Cricketer("Mushi" , 36,65,78,'BD')
Shakib.eat()
Shakib.exercise()
print(Shakib + Mushi)
print(Shakib * Mushi)
print(len(Shakib))
print(Shakib > Mushi)

#Plus Sign OverLoaded
print()
print(17+45)
print('Sakib' + 'Rakib')
print([12,98] + [5,6,7,1,2])