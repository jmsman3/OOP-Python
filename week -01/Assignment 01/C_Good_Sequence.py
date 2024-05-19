
N = int(input())
a = list(map(int, input().split()))
cnt = {}
for num in a:
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1
extra_result = 0
for num in cnt:
    if cnt[num] > num:
        extra_result += cnt[num] - num
    elif cnt[num] <num:
        extra_result +=  cnt[num]
print( extra_result)
