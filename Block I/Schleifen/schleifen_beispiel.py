# Wir wollen nur die geraden Zahlen als Schleife von 10 - 20 ausgeben lassen:

for zahl in range(10, 20):
    if zahl % 2 == 0:
        print(zahl)

# Wir fordern vom Benutzer solange eine Eingabe bis er Benutzer das Wort "Python" eingibt

such_wort = "Python"
user_input = str(input("Eingabe: "))

while user_input != such_wort:
    print("Nicht das gesuchte Wort!")
    user_input = str(input("Eingabe: "))
