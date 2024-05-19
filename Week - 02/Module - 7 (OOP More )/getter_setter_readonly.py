# Read only --> You cannot set the value ,value can not be changed
# Getter --> get a value of a property through a method , most of the time you will get the value of a Private attribute
# Setter --> Set a value of a property through a method , most of the time you will get the value of a private method


class user :
    def __init__(self,name ,age , money) -> None:
        self._name = name
        self._age= age
        self.__money = money
    
    #Read Only Attribute(Getter without any Setter)
    @property
    def age(self):
        return self._age 
    
    #Getter
    @property
    def salary(self):
        return self.__money
    
    #Setter
    @salary.setter
    def salary( self, value):
        if value <0 :
            return 'Salary can not be Negative'
        self.__money += value 
    

Samsu = user( 'Kopa', 21, 12000)
# print(Samsu.__money)
# print(Samsu.age())        #without @Property
print(Samsu.age)  #with @property
# print(Samsu.salary()) #without @Property
print(Samsu.salary)
Samsu.salary = 4500
print(Samsu.salary)