nums = input()

# for i in range(len(nums)):
#     if nums[i] != '0':
#         res = nums[i::]
#     Rivars_kora = res[::-1]
#     break
# else : 
#     res = '0'   #sobgula ZERO hoel res ZERO hobe
Rivars_kora = nums[::-1]
print(int(Rivars_kora))

if nums == Rivars_kora :
    print('YES')
else:
    print('NO')






 

