cars = ["audi", "bmw", "subaru", "toyota"]

for elem in cars:
    if(elem == "audi"):
        print("The car is an audi")
    else:
        print("The car is not an audi")

numericalList = [1,2,3,4,5]

for elem in numericalList:
    if elem == 1:
        print("The number is equal to one")


for elem in numericalList:
    if elem > 1 and elem <3:
        print("The number is equal to 2")
    
for elem in numericalList:
    if elem == 1 or elem == 3:
        print("The number is equal to 1 or to 3")

#Cascade conditions
for elem in numericalList:
    if elem == 1:
        print("The number is equal to 1")
    elif elem == 3:
        print("The number is equal to 3")
