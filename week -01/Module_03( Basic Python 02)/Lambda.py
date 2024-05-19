#Google : Python Map
#Goole : Python Built in Functions
#Lambda

# def double(x):
#     return x*2
# res= double(2) 
# print(res)     //ai function purata lambda deye easily lekha jai
#1
double = lambda num : num*2
Squared = lambda num : num * num
result = double(44)
output = Squared(9)
print(result, output)
#2
add = lambda x,y : x+y
sum = add(11,33)
print(sum)
#3
numbers = [ 10,56,25,14,53,477,89,5]
# double_num = map(double, numbers)
double_num = map( lambda x : x*2 , numbers)
squaredd_num = map(lambda x : x*x ,numbers )
print(numbers)
# print(list(double_num)) #21 no. line list e converest korle double hobe
print(list(squaredd_num))

#list of dictonary below
actors = [
    {'name' : 'Sabana' , 'age': 65},
    {'name': 'sabnoor', 'age': 45 },
    {'name': 'sabila noor', 'age': 30 },
    {'name': 'srabonti', 'age': 38 },
    {'name': 'shaon', 'age': 47 },
]

juniors = filter (lambda actors : actors['age'] <40, actors)
fivers = filter( lambda actors : actors ['age'] % 5 ==0 , actors)
print(list(juniors))
print(list(fivers))