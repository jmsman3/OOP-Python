def sum  (num1, num2, num3 = 0,num4 =0, num5 = 0):
    result = num1+ num2 + num3 + num4 + num5
    return result
total = sum(9,11,5)
# # print( 'total :', total)

def all_sum( num1, num2 ,*numbers):
    # print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum = sum+num
    return sum


total = all_sum( 10  ,20 ,30 ,40 ,50 ,60, 70, 80, 90, 100 )
print( 'All Sum :', total)
  

 