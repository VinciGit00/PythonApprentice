#Definition of a list
bicycles = ["trek", "bianchi", "cannondale", "specialized"]

#Accessing an element of a list
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[-1])

#Changing, adding and remove element in lists
#Modifying element to a list
bicycles[1] = "New name"

#Append at the end of the list
bicycles.append("appended element")

#Inserting an element to the list
#First element = index of the list 
bicycles.insert(0, "inserted element")
print(bicycles)

#Removing an element from the list
del bicycles[0]

#pop
#For just one element
variable = bicycles.pop(0)

#For all the list
newlist = bicycles.pop()

#Removing an item by value
bicycles.remove("cannondale")

#Sorting lists
#Ascendant
bicycles.sort()

#Descendant
bicycles.sort(reverse=True)

#Length of a list
size = len(bicycles)
print(size)