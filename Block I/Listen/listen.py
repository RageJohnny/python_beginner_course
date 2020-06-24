# Wir erstellen unsere erste Liste:

player_list = ["Dino", "Milan", "Michael", "Johnny"]
player_points = [10, 20, 30, 40]

# Wie greifen wir nun auf diese Liste zu?

# auf ein einzelnes Element:

print(player_list[0])  # GANZ WICHTIG! Listen beginnen immer mit dem Index 0

# über die ganze Liste iterieren:

for i in range(0, len(player_list)):
    print(player_list[i])

# wir können auch über mehrere Listen gleichzeitig iterieren:

for i in range (0, len(player_list)):
    print(player_list[i] + " has reached " + str(player_points[i]) + " Points in his final Python test")

# wir können auch mit Teillisten arbeiten:

Team_A = player_list[0:2]
Team_B = player_list[2:4]

print(Team_A)
print(Team_B)

# Listen können auch unterschiedliche Datentypen gleichzeitig enthalten:

new_player_points = [42, "keine", 2, "nicht teilgenommen"]

for i in range(0, len(Team_A)):
    print("Spieler: " +str(Team_A[i]) +" / "+ "Punkte: " +str(new_player_points[i]))

# wir können auch überprüfen ob ein gewisses Element in der Liste vorhanden ist oder nicht:

if "keine" in new_player_points:
    print("NOOB")

# wir können bestehenden Listen auch neue Elemente hinzufügen oder entfernen:

player_list.append("Paul")
print(player_list)
player_list.remove("Paul")
print(player_list)