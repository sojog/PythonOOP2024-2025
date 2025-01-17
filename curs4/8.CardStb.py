"""
Trebuie creată clasa STBCard care reprezintă cardul de la regia autonomă de transport București. 
Atributele necesare sunt: numele deținătorului, călătorii disponibile și creditul disponibil
În cazul in care nu primește numele deținătorului, setati-l automat pe "Nenominal"
Setați valoarea unei călătorii validate cu credit la 3 lei.
Creați funcții automate pentru validare cu credit/validare călătorie și reîncare credit/reîncarcare călătorii 
"""

class STBCard:
    VALOARE_CALATORIE = 3
    def __init__(self, nume = "Nenominal", calatorii = 0 , credit = 0):
        self.nume = nume
        self.calatorii = calatorii
        self.credit = credit

    def __str__(self):
        return f"{self.nume} are {self.calatorii} calatorii si {self.credit} lei credit"
    
    def validare_calatorie(self):
        if self.calatorii:
            self.calatorii -= 1
        elif self.credit >= STBCard.VALOARE_CALATORIE:
            self.credit -= STBCard.VALOARE_CALATORIE
        else:
            print("Esti pe blat!!!")

    def reincarcare_calatorii(self, calatorii_noi):
        self.calatorii += calatorii_noi

    def reincarcare_credit(self, credit):
        self.credit += credit
    
    def reincarcare(self, **kargs):
         self.calatorii += kargs.get('calatorii', 0)
         self.credit += kargs.get('credit', 0)

    def reincarcare_2(self, credit=0, calatorii_noi=0):
        self.credit += credit
        self.calatorii += calatorii_noi
        

card1 = STBCard("Ion Ionescu", 3, 3)
print(card1)
card2 = STBCard()
print(card2)
card3 = STBCard(credit=4)
print(card3)


card1.validare_calatorie()
print(card1)
card1.validare_calatorie()
print(card1)
card1.validare_calatorie()
print(card1)
card1.validare_calatorie()
print(card1)
card1.validare_calatorie()
print(card1)

card1.reincarcare(credit=10)
card1.reincarcare(calatorii=7)
print(card1)
card1.reincarcare(calatorii=1, credit=1)
print(card1)

card1.reincarcare()
print(card1)

card1.reincarcare()
print(card1)

card2.reincarcare_2(calatorii_noi=1, credit=1)
print(card2)