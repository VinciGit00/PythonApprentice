from Worker import Worker

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