A,B = list(map(int, input().split()))



found = False
for i in range( A, B+1):
    i_str = str(i)
    is_lucky = True
    for digit in i_str:
        if digit != '4' and digit != '7':
            is_lucky = False
            break 
    if is_lucky :
        print(i, end=" ")
        found = True
if not found :
    print('-1')
