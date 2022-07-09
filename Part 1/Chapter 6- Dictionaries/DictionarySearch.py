dict2 = {
    "p1": {
        "last_name": "Vinciguerra",
         "nickname":"vinci",
        "first_name": "Marco"
    },
   "p2": {
        "first_name": "Giuseppe",
        "last_name": "Loperfido",
        "nickname":"Peppino"
    },
    "p3": {
        "age": 21,
        "last_name": "Avizzano",
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

print(listnames)