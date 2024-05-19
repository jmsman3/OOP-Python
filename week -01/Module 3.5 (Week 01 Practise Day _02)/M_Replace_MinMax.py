num = int(input())
A = list(map(int,input().split()))
min_index = A.index(min(A)) #a er min indx and a er max index ber korlam then swap kore delam thats it
max_index = A.index(max(A))
A[min_index] , A[max_index] = A[max_index] , A[min_index]
# for i in A:
#     print( i , end = ' ')
print( *A)






























