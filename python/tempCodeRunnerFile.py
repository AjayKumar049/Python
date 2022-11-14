#Printing first 10 natural number
for index in range(1,11):
    print(index)


num = 10
print("The multiplication of Even multiple of number is")
for count in range(2,11,2):
    print(num,'x',count,'=' ,num*count)


num = 17
print("The multiplication of Odd multiple of odd number is:",num)
for count in range(1,11,2):
    print(num,'x',count,'=',num*count)



num = 6
fact = 1
for index in range(1,7):
    fact = fact*index
print(fact)


num = [1,2,3,4]
sum = 0
for x in num:
    sum = sum+x
print(sum)


car = ['BMW','Toyota','Ford','Jaguar']
for display in car:
    print(display)



for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()





