#Elements of arr in reverse order
#Initialize array     
arr = [1,6,9,10,7,19]    
print("Original array: ") 
for i in range(0, len(arr)):    
    print(arr[i])     
print("Array in reverse order: ")   
#Loop through the array in reverse order    
for i in range(len(arr)-1, -1, -1):     
    print(arr[i])