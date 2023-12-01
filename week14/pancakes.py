class Pancake:
    __slots__ = ["__weight", "__type"]
    
    def __init__(self, weight, type):
        self.__weight = weight
        self.__type = type

    def __str__(self):
        return "A " + self.__type + " Pancake that weighs " + str(self.__weight) + "lbs."
    def __repr__(self):
        return "Pancake\n   Type: " + self.__type +"\n   Weight: " + str(self.__weight) +"lbs" 





def main():
    pancake1 = Pancake(2.4, "Chocolate Chip")
    print(pancake1)
    print()
    print(repr(pancake1))
    
main()