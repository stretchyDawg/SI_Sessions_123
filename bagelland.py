class Bagel:
    __slots__ = ["type", "price"]
    toasted = False


    def __init__(self, type, price):
        self.type = type
        self.price = price

PLAIN_BAGEL = Bagel("Plain Bagel", 2.50)
EVERYTHING_BAGEL = Bagel("Everything Bagel", 2.75)
POPPY_SEED_BAGEL = Bagel("Poppy Seed Bagel", 2.75)

ALL_BAGELS = [PLAIN_BAGEL, EVERYTHING_BAGEL, POPPY_SEED_BAGEL]

def main():
    for bagel in ALL_BAGELS:
        print(bagel.type)

if __name__ == "__main__":
    main()