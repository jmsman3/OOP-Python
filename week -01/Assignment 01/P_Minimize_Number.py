num = int(input())
A = list(map(int, input().split()))

cnt = 0
while True:
    Even_Paisi = True
    for i in A:
        if i %2 != 0:
            Even_Paisi = False
            break
    if Even_Paisi :
        res_A = []
        for i in A:
            if i %2 ==0:
                res_A.append(i//2)
            else:
                res_A.append(i)
          
        A = res_A
        cnt = cnt +1
    else:
        break 
print(cnt)
       
    

                   
                    

        
