class Tier:

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, alter):
        self.__alter = alter

    def getAge(self):
        return self.__alter

    def setRace(self, rasse):
        self.__rasse = rasse

    def getRace(self):
        return self.__rasse


    def print_info(self):
        print(self.__name)
        print(self.__alter)
        print(self.__rasse)


def main():
    mein_Tier = Tier()
    mein_Tier.setName("Johnny")
    mein_Tier.setAge(10)
    mein_Tier.setRace("Schäferhund")
    mein_Tier.print_info()

main()
