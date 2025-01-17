
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
        if type(calatorii_noi) == int:
            self.calatorii += calatorii_noi
        else:
            print("Variabila calatorii_noi nu este de tip int")

    def reincarcare_credit(self, credit):
        if isinstance(credit, int):
            self.credit += credit
        else:
            print("Variabila credit nu este de tip int")

card = STBCard()
print(card)
card.validare_calatorie()

card.calatorii = 3
print(card)
card.validare_calatorie()
print(card)

card.reincarcare_calatorii("infinit")
print(card)

card.reincarcare_credit("infinit")
card.validare_calatorie()