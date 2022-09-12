print("Ajay")
print(type("Ajay"))

a = 50  
b = a  
print(id(a))  
print(id(b))  
# Reassigned variable a  
a = 500  
print(id(a))  

name = "Vijya"  
age = 20  
marks = 80.50  
  
print(name)  
print(age)  
print(marks) 

name = "A"  
Name = "B"  
naMe = "C"  
NAME = "D"  
n_a_m_e = "E"  
_name = "F"  
name_ = "G"  
_name_ = "H"  
na56me = "I"  
print(name,Name,naMe,NAME,n_a_m_e, NAME, n_a_m_e, _name, name_,_name, na56me)

#Assigning single value to multiple variables
a=k=w=50    
print(a)    
print(k)    
print(w) 

#Assigning multiple values to multiple variables
a,b,c=5,10,15    
print (a)   
print (b)    
print (c)    

#Local Variable
# Declaring a function  
def mul():  
    # Defining local variables. They has scope only within a function  
    a = 58  
    b = 155  
    c = a * b  
    print("The Mulitiply is:", c)  
  
# Calling a function  
mul()  

#GLObal Variable
# Declare a variable and initialize it  
x = 104 
  
# Global variable in function  
def mainFunction():  
    # printing a global variable  
    global x 
    print(x)  
    # modifying a global variable  
    x = 'Welcome To Global Variable in python'  
    print(x)  
  
mainFunction()  
print(x) 


# printing single value   
a = 7
print(a)  
print((a)) 

#Print Multiple Variables
a = 5  
b = 6  
# printing multiple variables  
print(a,b)  
# separate the variables by the comma  
print(1, 2, 3, 4, 5, 6, 7, 8)   
 



