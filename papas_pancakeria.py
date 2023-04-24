'''
Papa's Pancakeria SI Session Activity
@ChristianMorgado (Spring23)
'''
import node_stack
import node_queue
import random

MAX_SEATS = 10

#-------------------------------------Pancake Class-------------------------------------#
class Pancake:
    __slots__ = ["__type"]
    
    def __init__(self, type):
        self.__type = type

    def __str__(self):
        return self.__type + " Pancake"

PLAIN_PANCAKE = Pancake("Plain")   
BLUEBERRY_PANCAKE = Pancake("Blueberry")
RASPBERRY_PANCAKE = Pancake("Raspberry")
NUTELLA_PANCAKE= Pancake("Nutella")
PANCAKES = [PLAIN_PANCAKE, BLUEBERRY_PANCAKE, RASPBERRY_PANCAKE, NUTELLA_PANCAKE]

#-------------------------------------Customer Class-------------------------------------#
class Customer:
    __slots__ = ["__name", "__order_amount", "__pancakes"]

    def __init__(self, name, order_amount):
        self.__name = name
        self.__order_amount = order_amount
        self.__pancakes = node_stack.NodeStack()

    def finishedPancakes(self):
        return self.__pancakes.is_empty()

    def makeOrder(self):
        for order in range(self.__order_amount):
            self.__pancakes.push(PLAIN_PANCAKE)
    
    def eatPancake(self):
        try:
            self.__pancakes.pop()
        except:
            pass

    def __str__(self):
        return self.__name + str(self.__order_amount)      

#-------------------------------------Pancakeria Class-------------------------------------#
class Pancakeria:
    __slots__ = ["__name", "__in_restaurant", "__ordering", "__eating", "__max_seats", "__outside_line"]

    def __init__(self):
        self.__name = "Papa's Pancakeria"
        self.__in_restaurant = []
        self.__ordering = node_queue.NodeQueue()
        self.__eating = []
        self.__outside_line = node_queue.NodeQueue()
        self.__max_seats = MAX_SEATS

    def seatPerson(self, person):
        if len(self.__in_restaurant) >= self.__max_seats:
            self.__outside_line.enqueue(person)
        else:
            self.__in_restaurant.append(person)
            self.__ordering.enqueue(person)

    def unseatPerson(self, given_person):
        found_person = False
        for index in range(len(self.__in_restaurant)):
            person = self.__in_restaurant[index]
            if person == given_person:
                self.__in_restaurant.pop(index)
                found_person = True
                break

        for index in range(len(self.__eating)):
            person = self.__eating[index]
            if person == given_person:
                self.__eating.pop(index)
                found_person = True
                break

        while len(self.__in_restaurant) < self.__max_seats and not self.__outside_line.is_empty():
            try:
                person = self.__outside_line.dequeue()
                self.__in_restaurant.append(person)
                self.__ordering.enqueue(person)
            except:
                break
        if found_person == False:
            print("Invalid person.")

    def takeOrder(self):
        try:
            customer = self.__ordering.dequeue()
            customer.makeOrder()
            self.__eating.append(customer)

            for person in self.__eating:
                person.eatPancake()
                if person.finishedPancakes():
                    self.unseatPerson(person)
                
        except:
            pass
        if len(self.__in_restaurant) == 1 or len(self.__in_restaurant) == 2:
            for person in self.__in_restaurant:
                self.unseatPerson(person)


    def __str__(self):
        string =  self.__name + ":\n" + "\tPeople in restaurant: ["
        for person in self.__in_restaurant:
            string += str(person) + ", "
        string += "]\n\tPeople ordering: " + str(self.__ordering) + "\n" + "\tPeople eating: ["
        for person in self.__eating:
            string += str(person) + ", "
        string += "]\n\tPeople waiting outside: " + str(self.__outside_line) 
        
        return string


def main():
    
    # TESTING SEATING PEOPLE
    # people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # pancakeria = Pancakeria()
    # print(pancakeria)
    # for person in people:
    #     pancakeria.seatPerson(person)
    # print(pancakeria)
    # pancakeria.unseatPerson(2)
    # print(pancakeria)
    # pancakeria.unseatPerson(5)
    # print(pancakeria)
    # pancakeria.unseatPerson(4)
    # print(pancakeria)
    # pancakeria.unseatPerson(5) // Invalid Person
    # print(pancakeria)
    # pancakeria.unseatPerson(1)
    # print(pancakeria)
    # pancakeria.unseatPerson(7)
    # print(pancakeria)

    # TESTING PANCAKE STR
    # print(BLUEBERRY_PANCAKE)
    # print(RASPBERRY_PANCAKE)
    # print(NUTELLA_PANCAKE)
     
    people = []
    for _ in range(15):
        person = Customer("name", random.randrange(1, 4))
        people.append(person)

    pancakeria = Pancakeria()
    print(pancakeria)
    for person in people:
        pancakeria.seatPerson(person)
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)
    pancakeria.takeOrder()
    print(pancakeria)    
    pancakeria.takeOrder()
    print(pancakeria)


main()
