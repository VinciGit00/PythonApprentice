class Dog:
    #Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(str(self.name)+" is now sitting")
    
    def roll_over(self):
        print(self.name+" is now rolling")
    
    #Increment values
    def IncrementAge(self, number):
        self.age = self.age + number

#Instance of a class
Peppino = Dog("Peppino", 12)

#Getting the parameter of the class
print(Peppino.name)
print(Peppino.age)

#Calling methods
Peppino.sit()
Peppino.roll_over()
Peppino.IncrementAge(2)