# num , num1 = map(int, input().split())
# A = list(map(int, input().split()))

# for _ in range(num1):
#     L, R = map(int, input().split())
#     print( sum(A[L-1:R]))

num, num1 = map(int, input().split())
A = list(map(int, input().split()))

#  prefix sum
prefix_sums = [0] * (num + 1)
for i in range(1, num + 1):
    prefix_sums[i] = prefix_sums[i - 1] + A[i - 1]

# shesh queries
for _ in range(num1):
    L, R = map(int, input().split())
    print(prefix_sums[R] - prefix_sums[L - 1])
