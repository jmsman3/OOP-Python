import random 
from school import School 
class Person:
    def __init__(self, name) -> None:
        self.name = name 
    
class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def evalute_exam(self):
        return random.randint(50,100)
    
class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom #classroom object
        self.__id = None
        self.marks = {} #{"eng" : 78 , "math" : 90}
        self.subject_grade = {} #{"eng" : 'A' , "maht" : 'A+'}
        self.grade = None #final grade


    def calculate_final_grade(self) :
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade) #grade k value te converst kore felbe
            sum += point
        if sum == 0:
            grade = 0
            self.grade= 'F'
        else:
              gpa = sum/len(self.subject_grade)
              self.grade = School.value_to_grade(gpa)
        return f"{self.name} Final Grade : {self.grade} with GPA = {gpa}"
    


    
    #rahim.id == 
    #rahim.id = 12
    @property #aita getter
    def id (self) :
        return self.__id 
    
    @id.setter #aita setter
    def id(self, value):
        self.__id = value 










        
         
 








