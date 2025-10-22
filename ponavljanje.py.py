""""
broj = 10 # int (integer)
ime = "Pero" # string (string)
znak = 'a' # char (character)
cijena = 10.5 # float (decimalni broj)
istina = True # bool (boolean)

if broj > 5:
    print("Broj je veći od 5.")
elif broj == 5:
    print("Broj je jednak 5.")
else:
    print("Broj nije veći od 5.")

if istina:
    print("True")
else:
    print("False")
"""
#Zadatak 2
"""
print("Unesi temperaturu")
temperatura = int(input("Unesi temperaturu:"))
temperatura = input()
"""
"""
temperatura = int(input("Unesi temperaturu:"))
if temperatura <=  0:
    print("Ledenica")
elif temperatura > 0 and temperatura <= 15:
    print("Hladno")
elif temperatura > 15 and temperatura <= 25:
    print("Ugodno")
else:
    print("Vruće")
"""
#petlje
"""
for i in range(10):
    print(i)

for slovo in "Bok":
    print(slovo)

brojac = 0
while brojac < 11:
    print(brojac)
    brojac += 1
"""
#Zadatak 3
for broj in range(2, 21):
    if broj % 2 == 0:
        print(broj)
    else:
        continue

for broj in range(1, 21, 2):
    print(broj)

broj = 2
while broj <= 20:
    print(broj)
    broj += 2