#Tuple Methods 
Subjects = ('Physics', 'Chemistry','Maths')
Games = ('Football' , 'Tennis', 'Cricket')

#Indexing
print(Subjects[1])
print(Subjects.index('Maths'))

#Slicing
print(Games[0:2])

#Conactenation(Adding two list)
Subgames = Subjects + Games
print(Subgames)

##Repetition
print(Subjects*4)

#Count
print(Subjects.count('Chemistry'))

#Length
print(len(Subjects))


Subjects = [('Physics', 'Chemistry','Maths'),('Football' , 'Tennis', 'Cricket')]
print(Subjects[1][2])
print(Subjects[0][1])

Points = [(1,2),(3,4),(5,6)]
Points.append((8,7))
print(Points)

Points = [(1,2),(3,4),(5,6)]
Points.remove((1,2))
print(Points)

#String
chelsea = "Keep the blue flag flying high"
#Length
print(chelsea.__len__())
#Index
print(chelsea.index('b'))
#Count
print(chelsea.index('f'))
#Range
print(chelsea[0:4])
#Reverse
print(chelsea[::-1])
#upper
print(chelsea.upper())
#Multiple operator
print(chelsea * 2)
#Conactenation(Adding two tuples)
print(chelsea + "Lampard")
#Membership testing
if 'K' in chelsea:
    print("It is an element")

