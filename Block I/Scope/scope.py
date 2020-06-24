# Scope oder Gültigkeitsbereich ist ein wichtiger Bestandteil in der Programmierung.

#Beispiel:

def die_antwort_auf_alles():
    print(zahl)

def ein_teil_der_antwort():
    zahl = 7
    print(zahl)


zahl = 42
die_antwort_auf_alles()
ein_teil_der_antwort()