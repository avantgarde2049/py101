#static methods
class Milo:
    @staticmethod
    def printgood(string):
        print("the goods are:",string)


harry = Milo()
harry.printgood("Churan")#using instance

Milo.printgood("Babaji")#using class