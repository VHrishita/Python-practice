numbers = [1, 2, 2, 3, 4, 2, 5, 3]
mode = numbers[0]
max_count = 3

for i in numbers:
    count = numbers.count(i)
    if count > max_count:
        max_count = count
        mode = i
print("Mode is:", mode)
##== is for condition checking itself ''''''

'''arr = [1,2,3,4,5,6,7,2,2,2,2]
mode = max(arr, key=arr.count)
print("mode is", mode)
'''

