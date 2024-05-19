# import pyautogui
# from time import sleep

# num = int(input('Enter the number: '))
# sleep(0.65) 
# # print(num)
# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         sleep(0.50)              
#         pyautogui.write('#') 
#     pyautogui.press('Enter')           
#     sleep(0.20)      

    



# Read input
N = int(input())
a = list(map(int, input().split()))
cnt = {}
for num in a:
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1

excess_sum = 0
for num in cnt:  # Iterate through the keys of the cnt dictionary
    if cnt[num] > num:  # Compare the count of occurrences with the number itself
        excess_sum += cnt[num] - num  # Calculate excess occurrences

print(excess_sum)




































    