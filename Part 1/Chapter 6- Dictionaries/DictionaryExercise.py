
dict1 = {
    "p1": {
        "surname": "Vinciguerra",
        "first_name": "Marco",
        "nickname":"vinci"
    },
   "p2": {
        "surname": "Loperfido",
        "first_name": "Giuseppe",
        "nickname":"Peppino"
    },
    "p3": {
        "surname": "Avizzano",
        "first_name": "Claudia",
        "nickname":"Orsetta"
    }
}

#count the people with loperfido as last name
count = 0
names = []
flag = False
for elem in dict1.values():
    for key,value in elem.items():
        if(flag == True):
            #print(value)
            count = count + 1
            names.append(value)
            flag = False

        if(value == "Loperfido"):
          flag = True
#print(names)
#This piece of code is valid only with fixed structure, instead if you have a generic structure like this:
#PART2: generic dictionary
dict2 = {
    "p1": {
        "surname": "Vinciguerra",
         "nickname":"vinci",
        "first_name": "Marco"
    },
   "p2": {
        "first_name": "Giuseppe",
        "surname": "Loperfido",
        "nickname":"Peppino"
    },
    "p3": {
        "age": 21,
        "surname": "Avizzano",
        "first_name": "Claudia",
        "nickname":"Orsetta"
    }
}

listnames = []
progressive = 0
for elem in dict2.values():
    progressive = progressive+1
    for key, value in elem.items():
        if value == "Loperfido":
            counter = 0
            for elem in dict2.values():
                counter = counter+1
                for key, value in elem.items():
                    if(counter == progressive and key=="first_name"):
                         listnames.append(value)                       

#print(listnames)
                    
#Other method
list2 = []
for key, value in dict2.items():
    for key2, value2 in value.items():
        if(key2 == "surname" and value2 == "Loperfido"):
            list2.append(key)

print(list2)

for elem in list2:
    result = dict2[elem]["first_name"]
    print(result)


#Overriding of the keys
#If you add an element with the same key inside a dictionary it will be ovverided
dict1["p3"] = {
        "first_name": "Giuseppe",
        "surname": "Loperfido",
        "nickname":"Peppino"
    }, 
#print(dict1["p3"])
