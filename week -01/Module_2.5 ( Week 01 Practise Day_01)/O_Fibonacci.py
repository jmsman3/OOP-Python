
# def fb(n):
#     if n == 1:
#         return 0
#     elif n== 2:
#         return 1
#     else:
#         return fb(n-1) + fb(n-2)


    

nums = int(input())
fibo_nacci = []
if nums == 1 :
    print('0')
elif nums == 2:
    print('1')
else:
    fibo_nacci=[0,1]
    for i in range( 2, nums):
        res =fibo_nacci[i-1]+fibo_nacci[i-2]
        fibo_nacci.append(res)
    print(fibo_nacci[-1])




