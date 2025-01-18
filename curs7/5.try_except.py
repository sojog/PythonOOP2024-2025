x = 10
y = 0


## Tratamentul erori
try:
    rezultatul = x / y
    print("Rezultatul impartirii este:", rezultatul)
except:
    print("In acest caz exista o eroare")
finally:
    print("Aceasta linie se cheama oricum")
