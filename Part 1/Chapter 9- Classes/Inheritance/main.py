
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