class Zoo:
    totalAmountofAnimals = 0
    def __init__(self, name="default", amountOfAnimals=0, amountOfAviary=0, type="default", size="default"):
        self.name = name
        self.amountOfAnimals = amountOfAnimals
        self.amountOfAviary = amountOfAviary
        self.type = type
        self.size = size
        Zoo.totalAmountofAnimals += amountOfAnimals


    def toString(self):
        print("Name: " + self.name + ".  Amount of animals: ", self.amountOfAnimals,
          ". Amount of Aviaries: ", self.amountOfAviary, ". Type: " + self.type + ". Size: ", self.size, ".")


    def printSum(self):
        print("Quantity: " + self.name, self.amountOfAviary)


    @staticmethod
    def printStaticSum():
        print("All sum is" , Zoo.totalAmountofAnimals)

if __name__ == '__main__':
        zooTigers = Zoo("Tiger", 22, 5, "tiger", 'big')
        zooPenguins = Zoo()
        zooRhinos = Zoo("Rhino" , 14 , 8 , "rhino")


        zooTigers.toString()
        zooPenguins.toString()
        zooRhinos.toString()

        zooTigers.printSum()
        zooPenguins.printSum()
        zooRhinos.printSum()

        Zoo.printStaticSum()
