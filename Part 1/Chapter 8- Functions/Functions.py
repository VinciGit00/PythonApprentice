#Example of creation of a function

from re import A


def greet_user():
    print("Hello world")

greet_user()

def greet_user2(Username):
    print("Hello "+str(Username))

greet_user2("Franco")

#Default values
def describe_pet(pet_name, animal_type = "dog"):
    print(str(pet_name)+" "+str(animal_type))

#Using default values
describe_pet("Peppino")

#Not using default values
describe_pet("Peppino", "Hedgehog")

#Returning a value
def sum(a,b):
    return a+b

c = sum(2,1)

#Passing a list to a function
def greetingsList(names):
    for elem in names:
        print(elem)

usernames = ["Marco", "Franco", "Claudia"] 
greetingsList(usernames)