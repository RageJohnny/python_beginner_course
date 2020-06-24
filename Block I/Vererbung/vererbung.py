class Tier:

    def __init__(self, Name, Alter):
        self.name = Name
        self.alter = Alter

    def print_info(self):
        print(self.name)
        print(self.alter)


class Hund(Tier):

    def __init__(self, name, alter, rasse):
        super().__init__(name, alter)
        self.rasse = rasse

    def print_info(self):
        print(self.name)
        print(self.alter)#
        print(self.rasse)


def main():
    mein_Tier = Tier("Paul", 10)
    mein_Tier.print_info()

    mein_Hund = Hund("Johnny", 12, "Schäferhund")
    mein_Hund.print_info()


main()
