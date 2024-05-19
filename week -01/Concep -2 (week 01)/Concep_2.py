# lst = [1,2,3,4,5]
# print(lst[-2])

#remove duplicate
# lst = [1,2,2,3,4,5,65,4,4,6,5,65,14,4,5]
# lst = set(lst)
# lst = list(lst)
# print(lst)

#reverse python
# lst = lst[::-1]
# print(lst)

#Palindrom check
# a = "madam"  
# print( a == a[::-1])


# lst = [1,2,3,4,5,6,7,8,9,10]
# new_lst = list(filter(lambda x : x % 2 == 0, lst))
# print(list(new_lst))

# value = 5
# is_even = lambda x : x%2 ==0
# print(is_even(value))

#Count of list item
# lst = [1,1,2,2,2,3,3,3,3,4,4,5,5,5,6,6,4,7,8,8,9,5]
# dict = { item : lst.count(item) for item in lst}
# print()
# print(dict) 

# 5 er cheye boro value er index

# lst = [ 1,2,36,36,3,4,5,5,6,7,8,9,10]
# for i ,j in  enumerate(lst):
#     print(i , '-',j)
# value = 5
# new_lst1 = [i for i, j in enumerate(lst) if j > value]
# new_lst = [j for i, j in enumerate(lst) if j > value]
# index = print( new_lst1)
# val = print(new_lst)

#lsit merge kora

# dictt1= { 'rahim': 10, 'karim':20 , 'fahim' : 30}
# dictt2= { 'rahim': 2, 'karim':2 , 'sardar' : 3}
# result = dictt1

# for key, value in dictt2.items():
#     result[key] = result.get( key, 0) + value
# print(result)


#Even_value check in lst
# lst = [ 1,2,36,36,3,4,5,5,6,7,8,9,10] 
# def even_value(lst):
#     new_lst = []
#     for i in lst :
#         if i % 2 == 0:
#             new_lst.append(i)
#     return new_lst
# res = even_value(lst)
# print(res)

# lst = [ 1,2,36,36,3,4,5,5,6,7,8,9,10] 
# new_lst = list(filter(lambda x : x %2 ==0 , lst))
# print( new_lst)

#Even Odd Check Kora
# value = 5
# is_even = lambda x : x%2 == 0
# print( is_even(value))

#except , tey ,finally 
# try :
#     num1 = int(input('Number 01:- '))
#     num2 = int( input('Number 02:- '))
#     res = num1/num2
#     print( res)
# except ZeroDivisionError:
#     print( "Division by Zero is not Possible")
# except ValueError:
#     print( "Invalid Value")
# finally:
#     print( "End Of Program")



