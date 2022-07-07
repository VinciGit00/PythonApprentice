#Looping an entire list
magicians = ["alice", "silente", "carolina"]

#Iteration of all the elements in the list
for elem in magicians:
    print(elem)
print("End of the for loop")

#For loop with range
for i in range(1,5):
    print(i)
#The second part is not counted and the first instead yes

#Slicing a list

#Copying a list
a = magicians[1:2]
#2 excluded, 3 included
a = magicians[2:3]
print(a)

a = magicians[:]