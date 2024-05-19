class exam:
    Schooll = 'B_O_F_H_S'

    def __init__(self, marks):
        self.marks = marks 
    
    def After_Attend_Get_marks( self):
        self.marks = 33
    def before_attend_get_marks(self):
        self.marks = 'failed'

    def students( self, attedence):
        if attedence >0:
            print(f'Every Student will get {self.marks}')
        elif attedence <0:
            print(f'Every Student Will get { self.marks}')
        
my_exam = exam( 40)
my_exam.students( 12)
my_exam.students(-87) 
        

