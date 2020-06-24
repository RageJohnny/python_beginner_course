"""Aufgabe: Vom Benutzer soll eine Zahl eingeben werden können, welche im Anschluss daran überprüft wird ob es sich um die gesuchte Zahl handelt
#oder nicht. Falls ja, soll eine Ausgabe erfolgen, bei Nicht zu treffen soll der Nutzer darüber
informiert werden ob seine Zahl größer oder kleiner der gesuchten Zahl ist. """

lucky_number = 42

print("Bitte Zahl eingeben!")
user_input = int(input('>>'))

if user_input == lucky_number:
    print("Du hast die gesuchte Zahl erraten")
elif user_input < lucky_number:
    print("Die gesuchte Zahl ist größer als ", user_input)
else:
    print("Die gesuchte Zahl ist kleiner als ", user_input)
