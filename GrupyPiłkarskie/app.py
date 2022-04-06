import os
import random

kraj = ["Katar","Ekwador","Niemcy",
"Holandia","Anglia","Iran","USA",
"Walia","Argentyna","Arabia Saudyjska","Meksyk",
"Polska","Francja","Australia","Dania",
"Tunezja"]

liczba = 4
grupaA = []
grupaB = []
grupaC = []
grupaD = []


for i in range(liczba):
    rand = random.choice(kraj)
    grupaA.append(rand)
    kraj.remove(rand)

for i in range(liczba):
    rand = random.choice(kraj)
    grupaB.append(rand)
    kraj.remove(rand)

for i in range(liczba):
    rand = random.choice(kraj)
    grupaC.append(rand)
    kraj.remove(rand)

for i in range(liczba):
    rand = random.choice(kraj)
    grupaD.append(rand)
    kraj.remove(rand)

print(grupaA)
print(grupaB)
print(grupaC)
print(grupaD)