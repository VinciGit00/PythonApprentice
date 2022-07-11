
class Worker:
    def __init__(self, name, surname, role):
        self.name = name
        self.surname = surname
        self.role = role
    
    def printname(self):
        print(str(self.name)+" "+str(self.surname))

    def printrole(self):
        print(self.role)