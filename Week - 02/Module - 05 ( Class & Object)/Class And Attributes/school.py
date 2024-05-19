class student:
    def __init__(self, name , current_class , id):
        self.name = name 
        self.current_class = current_class
        self.id = id
    def __repr__(self) -> str:
        return f'Student with name :{self.name},class :{self.current_class},id: { self.id}'
    

class Teacher:
    def __init__(self,name , subject , id):
        self.name = name
        self.subject = subject 
        self.id = id
    def __repr__(self) -> str:
        return f'Teacher Name :{self.name} , Subject is : { self.subject} ,id: {self.id}'
    
# alia = student('Alia Torkari', 9 , 1)
# renveer = Teacher('Dourun beer', 'Algorithm', '101')
# print(alia)
# print(renveer)

class School:
    def __init__(self,name) -> None:
        self.name = name 
        self.teachers = []
        self.students = []
    def add_teacher ( self , name , subject):
        id = len(self.teachers)+101
        teacher = Teacher(name , subject ,id)
        self.teachers.append( teacher)
    
    def enroll( self, name, fee):
        if fee<6500:
            return f'Not Enough Money'
        else:
            id = len(self.students)+1
            Student = student(name , 'c', id)
            self.students.append(Student)
            return f'{name} is enrolled with id :{id} ,extra money {fee - 6500}'
    
    def __repr__(self) -> str:
        print('Welcom to', self.name)
        print( '----------Our Teachers-----------')
        for teacherr in self.teachers:
            print( teacherr)
        print( '-------------OUR Student--------------')
        for studentsss in self.students:
            print(studentsss)
        return f'All Done For None'
    
phitron = School('Phitron')
phitron.enroll( 'Alia', 5200)
phitron.enroll( 'rani', 8000)
phitron.enroll( 'Aiswariya', 7000)
phitron.enroll( 'vaijan', 900000)

phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decape', 'DS')
phitron.add_teacher('Aj', 'Database')

print( phitron)
































