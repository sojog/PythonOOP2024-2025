# Definiți o funcție Python care primește un string ca argument și returnează un nou string în care toate vocalele au fost eliminate 
vocale = "aeiouAEIOU"
input_string = "Salutare, ce mai faci?" 

## V1
rezultat = ""
for i in input_string:
    if i not in vocale:
        rezultat += i
print(rezultat)

## V2
for i in input_string:
    if i not in vocale:
        print(i, end="")


