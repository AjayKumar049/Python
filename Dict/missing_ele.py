#finding missing number element in array
arr = [6,5,3,4,2,6,2,9,10]
missing_elements = []
for ele in range(arr[0], arr[-1]+1):
    if ele not in arr:
        missing_elements.append(ele)
print(missing_elements)


