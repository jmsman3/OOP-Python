def multiple():
    return 3,4
print(multiple())
things = 'pen' , 'tripod','water bottle', 'charger','phone','webcame','sunglass'
print(type(things))
print(things[0])
print(things[-2])
print(things[3:6])
if 'phone' in things :
    print('exist')

for item in things:
    print(item)

# things[0]='wagon'
# print(things)

#ignore
print(len(things))
mega = ([2,3,4] , [6,8,9,5])
print(type(mega))
# print(mega[0])
# print(mega[1])
print(mega[-1])
print(mega[-2])
mega[0][1] = 666  # 0 tomo tuple er 1 no index e ekta maan bosabo
print(mega)