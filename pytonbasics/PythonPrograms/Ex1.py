# 1. Count odd and even numbers in list datatype
l1 = [1, 3, 43, 54, 32, 52, 44, 5, 55, 63, 6]
oddCount = 0
evenCount = 0
for i in l1:
    if i % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
print('Number of Odd numbers in the list is :'+str(oddCount))
print('Number of even numbers in the list is :'+str(evenCount))