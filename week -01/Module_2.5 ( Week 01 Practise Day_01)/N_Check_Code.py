def is_valid( A, B, S):
    if len(S) != A + B  + 1:
        return False
    if S[A] != '-':
        return False
    
    for i in range(A):
        if not S[i].isdigit():
            return False
    for i in range( A+1, len(S)):
        if not S[i].isdigit():
            return False
        
    return True
# -----------------------------------------------------------------
A,B = map( int, input().split())
S = input().strip()


if is_valid(A,B,S):
    print('Yes')
else:
   print('No')