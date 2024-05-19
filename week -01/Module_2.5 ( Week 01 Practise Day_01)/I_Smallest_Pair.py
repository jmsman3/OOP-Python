T = int(input())
for _ in range(T):

    n1 = int(input())
    array = list(map(int, input().split()))

    min_result = float('inf')
    
    for i in range(n1):
        for j in range( i+1, n1):
            ans = array[i]  + array[j] +j -i 
            min_result = min( min_result, ans)

    print(min_result)