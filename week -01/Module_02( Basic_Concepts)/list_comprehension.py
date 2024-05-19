
#Process_01
numbers = [45,87,90,85,14,26,81,70]
odds= []

for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
print(odds)

#ShortCUt for Process_01
# odd_nums = [num for num in numbers if num % 2 == 1]
odd_nums = [num for num in numbers if num % 2 == 1 if num%5 == 0]
print( odd_nums)
# ---------------------------------------------------------------------------------
#Process_02
players = ['sakib', 'musfiq', 'liton']
ages = [38,37,32]

age_comb = []
for player in players:
    print('Player:', player)
    for age in ages:
        print( player,age)
        age_comb.append([player, age])
print(age_comb)

#ShortCUt for Process_02
age_comb2 = [[player,age] for player in players for age in ages]
print( age_comb2)