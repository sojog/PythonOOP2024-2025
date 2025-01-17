"""Definiți clasa Motor conținând informații despre seria motorului, puterea acestuia și numărul de kilometri parcurși. 
Derivați din această clasă specializările MotorElectric și MotorBenzina, care aduc în plus informații privind bateria (% consumat din baterie la 1 km), respectiv consumul de combustibil în litri la suta de kilometri.
"""


class Motor:
    def __init__(self, serie, putere, km):
         ## cu 2 __ variabila privata
        self.__serie_motor = serie
        self.__putere_motor = putere
        ## cu 1 singur _ variabila interna (protecta)
        self._km_parcursi = km * 1000

    def __str__(self):
        return f" {self.serie} cu {self.putere} CP si {self.km} km"

    @property
    def serie(self):
        return self.__serie_motor

    @property
    def putere(self):
        return self.__putere_motor
    
    @property
    def km(self):
        return self._km_parcursi

class MotorElectric(Motor):
    def __init__(self, serie, putere, km, procent):
        super().__init__(serie, putere, km)
        self.__baterie = procent


class MotorBenzina(Motor):

    def __init__(self, serie, putere, km, consum, capacitate_rezervor, cantitate_rezervor):
        super().__init__(serie, putere, km)
        self.__consum = consum
        self.__capacitate_rezervor = capacitate_rezervor
        self.__cantitate_rezervor = cantitate_rezervor

    def __str__(self):
        return f"{super().__str__()} are consum de {self.consum}l/km \n in rezervor {self.cantitate}l"

    # motor += 100
    # motor = motor +  100

    def __iadd__(self, noi_km):
        cantitate_necesara = (noi_km * self.consum) / 100
        if self.cantitate >= cantitate_necesara:
            self.cantitate -= (noi_km * self.consum) / 100
            self._km_parcursi += noi_km
        else:
            self._km_parcursi += self.cantitate / (self.consum / 100)
            self.cantitate = 0

        print("cantitatea de inceput", self.cantitate)
        print("cantitea ce trebuie consumata", (noi_km * self.consum) / 100)
        return self
    
    def refill(self):
        self.cantitate = self.capacitate

    @property
    def consum(self):
        return self.__consum

    @property
    def capacitate(self):
        return self.__capacitate_rezervor
    
    @property
    def cantitate(self):
        return self.__cantitate_rezervor
    
    @cantitate.setter
    def cantitate(self, noua_valoare):
        if noua_valoare < 0:
            print("Pana prostului")
        elif noua_valoare > self.capacitate:
            print("Dai bezina pe jos")
        else:
            self.__cantitate_rezervor = noua_valoare
