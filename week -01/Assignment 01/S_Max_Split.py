S = input()
cnt_L = 0
cnt_R = 0
Res_String =[]

for i in S:
    if i == 'L':
        cnt_L = cnt_L +1
    else:
        cnt_R = cnt_R +1

    if cnt_L == cnt_R:
        Res_String.append(S[:cnt_L+cnt_R])
        S = S[cnt_L + cnt_R:]
       
        cnt_L = 0  #cnt abar reset kora
        cnt_R =0

print(len(Res_String))
for string in Res_String:
    print(string)