name = 'sakib\'s khan'
name2 = "sakib khan"
# multi string 
name3 = """ sakib khan Number one """

print(name2 ,name , name3 )

# String is a Sequence of Character

for char in name2 :
    print(char) 
print(name2[1])

print(name2[1:6])
print(name2[-3]) 
print(name2[::-1]) 

#mutable means changeble 
# immutable means you cannot change 
# name2[0] = 'R'
print(name2)
if 'khan' in name2:
    print('Exist')

print(name2.upper())
