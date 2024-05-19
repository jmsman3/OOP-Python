num1 = input('Give me your Mark:- ')
int_mark = int(num1)
if int_mark <= 100 and int_mark >= 90:
    print("Congratulaions,You Got Golden A+")
elif int_mark <= 89 and int_mark >= 80:
    print("Your Grade is :- A+")
elif int_mark <= 79 and int_mark >= 70:
    print("Your Grade is :- A")
elif int_mark <= 69 and int_mark >= 60:
    print( "Your Grade is :- A-")
elif int_mark <= 59 and int_mark >= 50:
    print("Your Grade is :- B")
elif int_mark <= 49 and int_mark >= 40:
    print("Your Grade is :- C")
elif int_mark <= 39 and int_mark >= 33:
    print("Your Grade is :- D")
else :
    print("Sorry ,You are Fail")
    