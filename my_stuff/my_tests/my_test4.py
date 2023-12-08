"""
Implement your solution to the practicum in this file.
@ChristianMorgado
"""

"""
1: A pancake is a food (..duh). There are multiple types on pancakes (chocolate chip, blueberry, raspberry, 
etc...). Pancakes also have a weight (in lbs) and a price (in $). A pancake is less than another pancake if 
its weight is less than the other pancake's weight. If their weight is the same then order them alphabetically. 
Pancakes should be able to be put in sets… (if you are confused on what this means then ask your peers or the 
SIs for some help).

Make a few global variable pancakes, here are some examples:
PLAIN_PANCAKE = Pancake(<insert your parameters here>)   
BLUEBERRY_PANCAKE = Pancake(...)
RASPBERRY_PANCAKE = Pancake(...)
NUTELLA_PANCAKE = Pancake(...)
If these examples are confusing feel free to ask for clarification.

"""
class Pancake:
    __slots__ = ["__weight", "__type", "__price"]
    
    def __init__(self, type, weight, price):
        self.__type = type
        self.__weight = weight
        self.__price = price

    def get_type(self):
        return self.__type
    def get_weight(self):
        return self.__weight
    def get_price(self):
        return self.__price

    #representation
    def __str__(self):
        return str(self.__weight) + "lbs "+ self.__type + " Pancake"
    def __repr__(self):
        return "Type: " + self.__type +"\nWeight: " + str(self.__weight) +"lbs\n\n" 
    
    #equality
    def __eq__(self, other):
        if type(self) == type(other):
            return (self.__type == other.__type) and (self.__weight == other.__weight)
        return False
    def __lt__(self, other):
        if type(self) == type(other):
            if (self.__weight == other.__weight):
                return (self.__type <= other.__type)  # Then sort alphabetically (a simple boolean statement like this does the work for you by comparing ASCII values)
            return (self.__weight <= other.__weight)  # Sort by weight only if the weight is different
        return False
    
    #other
    def __hash__(self):
        return hash(self.__type) + hash(self.__weight) + hash(self.__price) 

PLAIN_PANCAKE = Pancake("Plain", 2.3, 5)   
BLUEBERRY_PANCAKE = Pancake("Blueberry", 1.6, 6)
RASPBERRY_PANCAKE = Pancake("Raspberry", 1.4, 6)
NUTELLA_PANCAKE = Pancake("Nutella", 4.4, 10)

class Order:
    __slots__ = ["__requests"]
    
    def __init__(self, requests):
        self.__requests = requests
        
    def get_total_weight(self):
        total_weight = 0
        for amount in self.__requests:
            for _ in range(amount):
                total_weight += self.__requests[amount].get_weight()
        return total_weight
    
    def get_total_price(self):
        total_weight = 0
        for amount in self.__requests:
            for _ in range(amount):
                total_weight += self.__requests[amount].get_price()
        return total_weight
                
    def __str__(self):
        string = "Order:\n"
        for amount in self.__requests:
            string += "  " + str(amount) + "x " + str(self.__requests[amount].get_type()) + "\n"
        string += "Total Weight: " + str(self.get_total_weight()) + "lbs"
        string += "\nTotal Price: $" + str(self.get_total_price())
        return string

def main():
    """
    Use this function to manually test your code (if needed)
    """
    
    order1 = Order({2:BLUEBERRY_PANCAKE, 1:NUTELLA_PANCAKE})
    
    print(order1)
    # order1.get_total_weight()

if __name__ == "__main__":
    main()