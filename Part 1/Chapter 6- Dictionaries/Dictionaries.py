#Definition of a dictionary
alien_0 = {'color': 'green', 'points': 4}

print(alien_0['color'])

alien_0['x_position'] = 0
alien_0['y_position'] = 1

print(alien_0)

#Starting with an empty dictionary

alien = {}
alien['x_position'] = 2
alien['y_position'] = 1

#Using get() to Access Value
print_value = alien.get('x_position', "No points")
print(print_value)

print_value2 = alien.get('z_position', "No points find")
print(print_value2)

# Looping the elements through the keys
user_0 = {
    "usernme" : "mvincig11",
    "first" : "Marco", 
    "last" : "Vinciguerra",
    "Description" : "A person",
}

#VERY IMPORTANT
for key, value in user_0.items():
    print("key: "+str(key))
    print("value: "+str(value))

#Looping all the keys
for key in user_0.keys():
    print(key)

#Looping all the values of a dictionary
for values in user_0.values():
    print(values)

#Sorting a dictionary
sorted_dictionary = sorted(user_0)
print(sorted_dictionary)

#List in a dictionary
#Example of a list in a dictionary

pizza = {
    'crust' : "thick",
    'toppings': ['mushrooms', "extra cheese"]
}

for key, value in pizza.items():
    print(len(value))
    for elem in value:
        print(elem)
#Problem: when you have a not list it return a different dimension
#Solution: change the structure of the dictionary

pizza = {
    'crust' : ["thick"],
    'toppings': ['mushrooms', "extra cheese"]
}

for key, value in pizza.items():
    print(key)
    for elem in value:
        print(elem)

#Dictionary in a dictionary
users = {
    'aentsein': {
        "first" : "albert",
        "last" : "einstein",
        "location" : "princeton"
    }, 
    'mcurie': {
        "first" : "marie",
        "last" : "curie",
        "location" : "paris"
    }
}

for values in users.values():
    for key, elem in values.items():
        if key== "first":
            print(elem)

