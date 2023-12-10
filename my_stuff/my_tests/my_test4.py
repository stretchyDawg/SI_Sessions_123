import node_queue
import node_stack
import csv

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
...

When making your pancakes, follow some standards when making prices (this is required for #4):
Plain Pancake: $2.50
Blueberry Pancake: $3.00
Mini Pancake: $1.50
Nutella Pancake: $5.50
Any other pancake: $4.00

If these examples are confusing feel free to ask for clarification.
"""
class Pancake:
    __slots__ = ["__weight", "__type", "__price"]
    
    def __init__(self, type, weight, price):
        self.__type = type
        self.__weight = weight
        self.__price = price

    def getType(self):
        return self.__type
    def getWeight(self):
        return self.__weight
    def getPrice(self):
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

PLAIN_PANCAKE = Pancake("Plain", 2.54, 2.50)   
BLUEBERRY_PANCAKE = Pancake("Blueberry", 1.6, 3.00)
RASPBERRY_PANCAKE = Pancake("Raspberry", 1.4, 4.00)
NUTELLA_PANCAKE = Pancake("Nutella", 4.4, 5.50)


"""
2: An Order contains the pancakes requested and the amount of pancakes requested. For example, an order should be able to 
articulate that 2 Chocolate Chip Pancakes and 1 Blueberry Pancake is requested. 

Find a data structure to represent this. You can pass in this data structure in the main function, (say you used a list, 
you can just pass in the list representing the pancakes in the main function). If it helps, you can manually test it in 
the main function, or if you wanna get crazy then make some unit tests! 

Requirements:
- There should be a method that returns the total price of the order 
- There should be a method that returns the total weight. 
- There should be a getter for the pancakes and the amount of pancakes requested.
- There should be a __str__ method that returns the data in this format:
    1 x Blueberry Pancake
    2 x Raspberry Pancake
    Total cost: <amount>lbs
    Total weight: $<amount>
"""
class Order:
    __slots__ = ["__requests"]
    
    def __init__(self, requests):
        self.__requests = requests
        
    def getRequests(self):
        return self.__requests
        
    def getTotalWeight(self):
        total_weight = 0
        for pancake in self.__requests:
            for _ in range(self.__requests[pancake]):
                total_weight += pancake.getWeight()
        return total_weight
    
    def getTotalPrice(self):
        total_price = 0
        for pancake in self.__requests:
            for _ in range(self.__requests[pancake]):
                total_price += pancake.getPrice()
        return total_price
                
    def __str__(self):
        string = ""
        for pancake in self.__requests:
            string += "  " + str(self.__requests[pancake]) + "x " + str(pancake.getType()) + "\n"
        string += "Total Weight: " + str(self.getTotalWeight()) + "lbs"
        string += "\nTotal Price: $" + str(self.getTotalPrice())
        return string
    
    
"""
3: A Pancakeria is a restaurant that takes in orders. They take in orders in first-come-first-serve manner. They serve pancakes in an 'eatable' fashion. 
Pancakes are eaten from the top down. After creating your __init__ function, provide these functionalities:
- A take_order method that... takes an order (adds it to the first-come-first-serve line).
- A serve pancake method that takes the order next in line and returns the pancakes requested from the order
  next in line in an 'eatable' fashion (pancakes are eaten from the top down)
- A print_next_order method that prints the next order in this format:
    Next Order:
        <next order information>
"""
class Pancakeria:
    __slots__ = ["__orders"]
    
    def __init__(self):
        self.__orders = node_queue.Queue()
        
    def printNextOrder(self):
        print("Next Order:\n", self.__orders.front(), sep = "")
        
    def takeOrder(self, order):
        self.__orders.enqueue(order)    
    
    def servePancake(self):
        order = self.__orders.dequeue()
        pancakes = node_stack.Stack()
        for pancake in order.getRequests():
            amount = order.getRequests()[pancake]
            for _ in range(amount):
                pancakes.push(pancake)
        return pancakes
            
        
"""
4: The local elementary school is having a Pancake party! They have a LOT of orders to make (10!), and instead of sending in 
their orders in a traditional fashion, they're sending their order as one submission in as a csv file in this format:

amount,type,weight
3,Plain,1.23
4,Plain,3.42
2,Blueberry,5.67
5,Nutella,1.23
6,Plain,4.75
1,Mini,24.9
2,Blueberry,1.2
3,Plain,6.8
1,Rainbow,3.4
4,Plain,5.6
(for testing, i recommend you copy this and make a order.csv file)

Note the pricing standards set in question #1:
Plain Pancake: $2.50
Blueberry Pancake: $3.00
Mini Pancake: $1.50
Nutella Pancake: $5.50
Any other pancake: $4.00

Make an 'order_csv(filename)' function that, based on this data, creates an Order instance with every pancake. The order should 
print in this format (assuming you have the correct __str__ method for the Order class):
"""
def order_csv(filename):
    requests = dict()
    
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for record in csv_reader:
            amount = record[0]
            pancake_type = record[1]
            weight = record[2]
            price = 0
            if pancake_type == "Plain":
                price = 2.50
            elif pancake_type == "Blueberry":
                price = 3.00
            elif pancake_type == "Mini":
                price = 1.50
            elif pancake_type == "Nutella":
                price = 5.50
            else:
                price = 4.00
            
            pancake = Pancake(pancake_type, float(weight), float(price))
            requests[pancake] = int(amount)

    return Order(requests)    

def main():
    """
    Use this function to manually test your code (if needed)
    """
    pancakeria = Pancakeria()
    order = Order({BLUEBERRY_PANCAKE:2, NUTELLA_PANCAKE:1, PLAIN_PANCAKE:2})
    
    pancakeria.takeOrder(order)
    pancakeria.printNextOrder()
    pancakes = pancakeria.servePancake()
    print(pancakes)
    print()
    print(order_csv("order.csv"))
    
    
    
    # order1.get_total_weight()

if __name__ == "__main__":
    main()