def full_name(first,last):
    name = f'full name is: {first} {last}'
    return name
# name = full_name('alu', 'kodu')
name = full_name(last = 'kodu', first=  'alu')
print(name)


def famous_name( first, last, **addition):
    name = f'{first} {last}'
    # print(addition['title'])
    for key,value in addition.items():
        print(key,value)
    return name

name = famous_name( first = 'taheri', last = 'ali', titlee = 'hujur',
title2 = 'sayakh', last2 = 'tahar')
print(name)     
        

def a_lot ( num1, num2):
    sum = num1+num2
    mult = num1*num2
    remain = num1-num2
    # return sum, mult,remain
    return [sum, mult,remain]  #list akar e o deya jai
everthing = a_lot(55,21)
print(everthing)



    