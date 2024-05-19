num = [26,12, 14, 98, 68]
num.append(56)
print(num)

num.insert(0 ,71)
num.insert(2, 81)
print(num)

if 98 in num :
    num.remove(98) 
if 8 in num:
    num.remove(8)
print(num)

last = num.pop()
print( last, num)

if 98 in num:
#     # index = num.index(5) //5 list e nai
    index = num.index(98)
    print(index)


Sorted = num.sort()
print(num)

Reverse = num.reverse()
print(num)