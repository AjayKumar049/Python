marks = int(input("Enter the marks:"))
if marks>=90:
    print("congrats! you scroed A Grade")
elif marks>=60 and marks<=80:
    print("congrats! you scroed B Grade")
elif marks>=50 and marks<=60:
    print("congrats! you scroed c Grade")
elif marks>=40 and marks<=50:
    print("congrats! you scroed D Grade")

else:
    print("You are Fail")

for i in range(1,10):
    print("ajay")

num =2
squ = num**2
print(squ)

p = 345
t = 24
r = 2.5
cal = p*t*r/100
print(cal)

from  array import *
array1 = array('i',[10,20,25,65])
for x in array1:
    print(x)


from  array import *
array1 = array('i',[10,20,25,65])
array1.insert(1,77)
for x in array1:
    print(x)


from  array import *
array2 = array('i',[10,20,25,65])
array2.remove(20)
for x in array2:
    print(x)



    


