my_array = [7, 12, 2,9, 4, 11, 1,8]
minVal = my_array[0]
print(minVal)
for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)
