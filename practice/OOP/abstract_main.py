from abstract_subclasses import *

splendor = Bike(2, "Blue")
splendor.display()

scooty = Scooter(2)
print(scooty.number_tyres)

etios = Car(4)
print(etios.number_tyres)

splendor.start()
scooty.start()
etios.start()