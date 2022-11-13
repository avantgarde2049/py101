class Dad():
    soccer = 1
    dance = 3

class Son(Dad):
    soccer = 6
    dance= 1

    def dances(self):
        return f"I dance {self.dance} number of ways"

class Grandkid(Son):
    dance =4

    def dances(self):
        return f"I dance {self.dance} number of ways"

daddy=Dad()
sonny=Son()
jimmy=Grandkid()

print(Grandkid.dance)
print(Grandkid.soccer)#if attribute not found in itseld ,searches for the the next inheritance step which is Son
print(sonny.dances())
