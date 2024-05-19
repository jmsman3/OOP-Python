numbers = [12,56,98,78,56,12,26,98]
person1 = [ 'kalachan', 'kalipur', 23, 'student']
#key value pair
#Dictionary
#object
#hash table
#Overlap with Set
# { key : value, key:value, key:value}
person = { 'name' : 'Kala Pakhi', 'Address':'kalipur',
          'Age':23 ,'job':'facebookaer'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())

person['Language'] = 'Python'  #Add {key : Value}
# print(person)
person['Name2'] = 'Sada Pakhi' #Add { Key: value}
print(person)

#Special Dictionary Looping

for key ,value in person.items():
    print(key,value)