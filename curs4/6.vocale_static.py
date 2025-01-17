class ProcesatorText:
    # variabila statica
    VOCALE = "aeiouAEIOU"
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text
    
    def elimina_vocale(self):
        rezultat = ""
        for i in self.text:
            if i not in ProcesatorText.VOCALE:
                rezultat += i
        return rezultat


procesator = ProcesatorText("La multi ani!!!")
print(procesator)

print(procesator.elimina_vocale())
print(procesator.elimina_vocale())

print(ProcesatorText.VOCALE)