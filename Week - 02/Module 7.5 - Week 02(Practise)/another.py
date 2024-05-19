from datetime import date
class Person:
    def __init__(self, name , age) -> None:
        self.name = name 
        self.age = age
    
    @classmethod
    def Birth_year_Now( cls, name, Year):
        return f" His Name is:- {name} and Year:{ date.today().year-Year}"
    @staticmethod
    def adult( age):
        if age>18 :
            print('Adult')
        else:
            print("Not Adult")

Person1 = Person('Jubaer' ,22)
birth_year = Person1.Birth_year_Now( 'Jubar' , 22)
print(birth_year)

Age_status = Person1.adult(22)
print(Age_status)


    