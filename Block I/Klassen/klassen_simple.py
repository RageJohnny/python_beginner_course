class Tier:

    def __init__(self, Name, Alter):
        self.name = Name
        self.alter = Alter

    def print_info(self):
        print(self.name)
        print(self.alter)





def main():
    mein_Tier = Tier("Paul", 10)
    mein_Tier.print_info()


main()
