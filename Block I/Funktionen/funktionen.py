# Funktionen in Python werden grundsätzlich immer mit "def" initialisiert.

# Als Beispiel werden wir hier alle Grundrechnungsarten als eigene Funktion schreiben

def addition(zahl1, zahl2):
    return print(zahl1 + zahl2)


def subtraktion(zahl1, zahl2):
    return print(zahl1 - zahl2)


def multiplikation(zahl1, zahl2):
    return print(zahl1 * zahl2)


def division(zahl1, zahl2):
    return print(zahl1 / zahl2)


addition(10, 5)
subtraktion(10, 5)
multiplikation(10, 5)
division(10, 5)


# Das ganze können wir nun auch mit Usereingaben erweitern:

def addition_extended():
    input1 = int(input("Zahl 1: "))
    input2 = int(input("Zahl 2: "))
    ergebnis = input1 + input2
    return print(ergebnis)

addition_extended()