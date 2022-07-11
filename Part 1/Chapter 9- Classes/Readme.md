# Chapter 9- classes

## Introduction

Object oriented programming is one of the most effective approaches to writing software. Classes represent the real word things and situations

## Creating and using a class

### Constructor

```python
def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Example of a complete class

```python
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
```

## Making an instance of a class

```python
Peppino = Dog("Peppino", 12)
```

## Getting the parameter of the class

```python
print(Peppino.name)
print(Peppino.age)
```

## Calling methods

```python
Peppino.sit()
Peppino.roll_over()
```
