# Inheritance

Python inheritance. In python is possible to create parent classes and child classes.

## Import classes

```dart
from Worker import Worker
```

## Parent class

```python
class Worker:
    def __init__(self, name, surname, role):
        self.name = name
        self.surname = surname
        self.role = role

    def printname(self):
        print(str(self.name)+" "+str(self.surname))

    def printrole(self):
        print(self.role)
```

## Child class

Derived class

```python
class SpecializedWorker(Worker):
    def __init__(self, name, surname, role, age, factory):
        super().__init__(name, surname, role)
        self.age = age
        self.factory = factory

    def getProperties(self):
        print(str(self.name)+" "+str(self.surname)+" "+ str(self.age)+" "+str(self.factory))

    #Overrifing of the method printname
    def printname(self):
       return super().printname()

     #Overrifing of the method printname
    def printrole(self):
       print(self.role+" "+ self.factory)
```

## Main class

```python
from Specialized_worker import SpecializedWorker
from Worker import Worker

if __name__ == "__main__":
    w = Worker("Marco", "Vinciguerra", "AD")
    w.printname()
    w.printrole()

    w2 = SpecializedWorker("Marco", "Vinciguerra", "ruolo", "22", "factory")
    w2.printname()
    w2.printrole()
else:
    print ("Executed when imported")
```
