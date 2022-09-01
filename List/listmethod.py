#List Methods 
Subjects = ['Physics', 'Chemistry','Maths']
Games = ['Football' , 'Tennis', 'Cricket']
#Append
Subjects.append('Biology')
print(Subjects)
#Insert
Subjects.insert(1, 'History')
print(Subjects)
#Extend
Subjects.extend(Games)
print(Subjects)
#Remove
Subjects.remove('Chemistry')
print(Subjects)
#Reverse
Subjects.reverse()
print(Subjects)
#Conactenation(Adding two list)
print(Subjects + Games)
#Repetition
print(Subjects * 2)
#Length
print(len(Subjects))
print(len(Games))
#Index
print(Subjects[1])
print(Subjects[1:6])
print(Subjects[-5])
#Sort
Subjects.sort()
print(Subjects)
