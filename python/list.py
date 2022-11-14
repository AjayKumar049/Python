list = ['ajay',145,12+6j,2.8,13]
sub = ['physics','history','Biology']
print(list)

#append - adding new values in last index
list.append(127)
print(list)

#insrt - adding new values in the index number one
list.insert(1,17)
print(list)

#remove 
list.remove('ajay')
print(list)

#conactenation
print(list + sub)


#reverse
list.reverse()
print(list)

#extend - acts like conactenation
list.extend(sub)
print(list)