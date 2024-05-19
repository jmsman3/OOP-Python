# # Input the number of elements in the array
# N = int(input())

# # Input the array elements
# array = list(map(int, input().split()))

# # Find the minimum and maximum elements and their indices
# min_element = min(array)
# max_element = max(array)
# min_index = array.index(min_element)
# max_index = array.index(max_element)

# # Swap the minimum and maximum elements
# array[min_index], array[max_index] = max_element, min_element

# # Output the modified array
# print(*array)

num1 = int(input())
array = list(map(int, input().split()))

min_index = array.index(min(array))
max_index = array.index(max(array))

array[min_index],array[max_index] = array[max_index] , array[min_index]

# for res in array:
#     print( res, end = " ")

print(*array)





























