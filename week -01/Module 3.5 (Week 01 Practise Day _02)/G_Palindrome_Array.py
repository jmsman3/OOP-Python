# num = int(input())
# A = list(map(int, input().split()))
# left = 0
# right = num-1 

# while left <right:
#     if A[left] != A[right]:
#         print('NO')
#         break
#     left = left +1
#     right = right -1
# else:
#     print('YES')


num = int(input())
A = list(map(int, input().split()))
B = A[::-1]
if A == B:
    print('YES')
else:
    print('NO')
















