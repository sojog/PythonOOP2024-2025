
from motor import Motor, MotorBenzina, MotorElectric


# masina1 = MotorBenzina("qwerty", 70, 180, 5)
# print(masina1)

bmw = MotorBenzina("B58", 320, 218, 13, 60, 7)
print(bmw)

bmw += 100
print(bmw)

bmw.refill()
print(bmw)

bmw += 100
print(bmw)

bmw += 100
print(bmw)