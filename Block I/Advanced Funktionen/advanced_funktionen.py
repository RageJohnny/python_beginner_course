def adress(name, stadt, strasse, nummer, land="Österreich", anmerkung=""):
    print("\n------")
    print(name)
    print("Wohnhaft:")
    print(stadt)
    print(strasse + " " + nummer)
    print(land)  #
    print(anmerkung)
    print("\n------")


adress("Johnny", "XY", "XY", "3")
adress("Johnny", "XY", "XY", "3", land="Deutschland", anmerkung="Bring euch Pyhton bei!")
