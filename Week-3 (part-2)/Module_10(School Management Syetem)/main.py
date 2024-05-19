from subject import Subject
from school import School
from person import Student, Teacher
from classroom import ClassRoom

school = School("ABC", "Dhaka")

# Adding Classrooms
eight = ClassRoom("Eight")
Nine = ClassRoom("Nine")
Ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(Nine)
school.add_classroom(Ten)

# Adding Students
rahim = Student("Rahim", eight)
karim = Student("Karim", Nine)
fahim = Student("Fahim", Ten)
hamim = Student("Hamim", Ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)

# Adding Teachers
abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
kabul = Teacher("Kabul Khan")

# Adding Subjects
bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", kabul)
biology = Subject("Biology", babul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)

Nine.add_subject(biology)
Nine.add_subject(physics)
Nine.add_subject(chemistry)

Ten.add_subject(chemistry)
Ten.add_subject(physics)
Ten.add_subject(bangla)
Ten.add_subject(biology)

eight.take_semester_final_Exam()
Nine.take_semester_final_Exam()
Ten.take_semester_final_Exam()

print(school)
