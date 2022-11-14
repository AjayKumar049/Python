#Printing first 10 natural number
for index in range(1,11):
    print(index)

#Printing Even multiple of even number 
num = 10
print("The multiplication of Even multiple of number is")
for count in range(2,11,2):
    print(num,'x',count,'=' ,num*count)

#Printing Odd multiple of odd number
num = 17
print("The multiplication of Odd multiple of odd number is:",num)
for count in range(1,11,2):
    print(num,'x',count,'=',num*count)


#Calculating the factorial of a given number
num = 6
fact = 1
for index in range(1,7):
    fact = fact*index
print(fact)

#Addition of all list of elements 
num = [1,2,3,4]
sum = 0
for x in num:
    sum = sum+x
print(sum)

#Displaying the list one to one another 
car = ['BMW','Toyota','Ford','Jaguar']
for display in car:
    print(display)


#Printing the star Pattern
for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()


# Python Numeric Pattern Example 2
for i in range(0, 5):
    num = 1
    for j in range(0, i+1):
        print(num, end=" ")
        num = num + 1
    print()

#Reverse Numeric pattern
for i in range(5, 0, -1):
    for j in range(0, i):
        print(i, end="")
    print()









