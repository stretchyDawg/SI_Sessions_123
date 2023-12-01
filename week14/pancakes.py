import random
import node_stack

class Pancake:
    __slots__ = ["__weight", "__type"]
    
    def __init__(self, weight, type):
        self.__weight = weight
        self.__type = type

    def get_weight(self):
        return self.__weight

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
        return hash(self.__type) + hash(self.__weight)
    
    
    
    
    
class Pancakes:
    __slots__ = ["__pancakes", "__total_weight"]
    
    def __init__(self):
        self.__pancakes = node_stack.NodeStack()
        self.__total_weight = 0
        
    def add_pancake(self, pancake):
        self.__pancakes.push(pancake)
        self.__total_weight += pancake.get_weight()
        
    def eat_pancake(self):
        if not self.__pancakes.is_empty():
            pancake = self.__pancakes.pop()
            self.__total_weight -= pancake.get_weight()
        else:
            raise IndexError("NO MORE PANCAKES :C")
        
    def __lt__(self, other):
        if type(self) == type(other):
            return (self.__total_weight <= other.__total_weight)
        return False
    
    def __str__(self):
        # The round function rounds the number to 1 decimal, you don't need it (and don't use it on your homework)
        return str(self.__pancakes) +"\nTotal Weight: " + str(round(self.__total_weight, 2)) + "\n"
        
        
        

    

def main():
    # FOR TESTING, COMMENT OUT THE BLOCKS OF CODE YOU DON'T WANT
    
    pancake1 = Pancake(2.4, "Chocolate Chip")
    print(pancake1)
    print()
    print(repr(pancake1))

    pan2 = Pancake(1.2, "Banana")
    pan3 = Pancake(0.2, "Strawberry")
    pan4 = Pancake(3.6, "Plain")
    pan5 = Pancake(7.9, "Jumbo")
    pan6 = Pancake(3.6, "Plain")
    pan7 = Pancake(0.2, "Jumbo")
    
    # The sort() function uses __lt__, so I'm using it to show that our __lt__ and __eq__ methods work:
    print("\nUnsorted")
    pancakes = [pancake1, pan2, pan3, pan4, pan5, pan6, pan7]
    print(repr(pancakes))
    print("\nSorted:")
    pancakes.sort()
    print(repr(pancakes))
    # I know the formatting looks weird but you should get the idea... it sorts by weight THEN sorts alphabetically
    
    # Proof pancakes can be used in a set
    print("\nSet")
    set_pancakes = set(pancakes)
    print(repr(set_pancakes))
    print()
    
    # IMPORTANT TIP:
    # If you want proof that you need a hash function to put things in sets,
    # comment out the pancake hash function and run this file again, you'll 
    # see that you'll get an error when you try to create the set.
    
    
    #------ Pancakes Class ------
    print("Pancakes Class")
    pancakes_class = Pancakes()
    print(pancakes_class)
    pancakes_class.add_pancake(pancake1)
    print(pancakes_class)
    pancakes_class.add_pancake(pan2)
    print(pancakes_class)
    pancakes_class.add_pancake(pan3)
    print(pancakes_class)    
    pancakes_class.add_pancake(pan4)
    print(pancakes_class)
    
    pancakes_class.eat_pancake()
    print(pancakes_class)

    
main()