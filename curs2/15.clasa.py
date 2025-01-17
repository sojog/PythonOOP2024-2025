import math

class Cerc:
    def __init__(self, raza):
        self.raza = raza

    # functia prin care se face convert de la obiect la str
    def __str__(self):
         return f"Perimetru: {self.perimetru()} \nAria:{ self.aria()} \nDiametru {self.diametru()}"
         #return "Acesta este un string  hardcodat care apare in functia ___str__ din clasa Cerc. Unde oare va fi printat acest string????"

    def perimetru(self):
        return 2 * math.pi * self.raza

    def aria(self):
        return math.pi * self.raza ** 2

    def diametru(self):
        return self.raza * 2
    
    def arata_valorile(self):
        print("Perimetru:", self.perimetru())
        print("Aria:", self.aria())
        print("Diametru", self.diametru())


cerc1 = Cerc(1)
print(cerc1)


cerc2 = Cerc(2)
print(cerc2)