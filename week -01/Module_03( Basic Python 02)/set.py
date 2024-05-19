#Google : python set methods
#list --> []
#tuple --> ()
#set --> {}
#So, Set is Unique items Collection, Not duplicate
numbers = [10,56,98,78,56,12,6,98]
print(numbers)
number_set = set(numbers)
print(number_set)
number_set.add(55)
# print(number_set)
number_set.add(12) # 12 theke 14 line ek e element bar bar Set er moddhe Add kora jai na
number_set.add(12)
number_set.add(12)
print(number_set)
number_set.remove(6)
print(number_set)
# number_set[1] = SET THEKE ADD OTHOBA REMOVE KORA JABE ,BUT KON PARTICULAR INDEX E NOTUN VALUE ASSIGN KORA JABE NA
# print(number_set)
for item in number_set:
    print(item)
    
if 9 in number_set:
    print('9 exist')    #kono output debve na karon kono 9 nai 
elif 98 in number_set:
    print('98 exist')

A = { 1,3,5,7}
B = { 1,2,3,4,5}
print(A & B)
print( A | B) # A U B mane A r B er Sob e print korbe
