class Node:
    __slots__ = ["__value", "__next"]

    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next

    def get_value(self):
        return self.__value
    def set_value(self, value):
        self.__value = value

    def get_next(self):
        return self.__next
    def set_next(self, next):
        self.__next = next
        
    def length(self):
        length = 0
        while self is not None:
            self = self.get_next()
            length += 1
        return length
        
    def __str__(self):
        return str(self.__value) + " -> " + str(self.__next)

        
# made in 2022, highlights the recursive nature of the str function above (2023 class had better methods, shown above)
def print_node(node):
    if node is None:
        print(None)
    else:
        value = node.get_value()
        print(str(value), "-> ", end = "") 
        print_node(node.get_next())

        
def length(node):
    # if node is None:
    #     return 0
    # else: 
    #     rest = length(node.get_next())
    #     return rest + 1

    count = 0
    while node is not None:
        node = node.get_next()
        count += 1
    return count

def length2(node, count=0):
    """recursive"""
    if node is None:
        return count
    else:
        count += 1
        next = node.get_next()
        return length2(next, count)
    
def recursive_sum(node, sum=0):
    if node is None:
        return sum
    else:
        sum += node.get_value()
        return recursive_sum(node.get_next(), sum)

def main():
    node_a = Node("a")           # None
    print_node(node_a)    
    node_b = Node("b", node_a)   # a -> None
    print_node(node_b)    
    node_c = Node("c", node_b)   # b -> a -> None
    print_node(node_c)    
    node_d = Node("d", node_c)   # c -> b -> a -> None
    print_node(node_d)    
    node_e = Node("e", node_d)   # d -> c -> b -> a -> None
    print_node(node_e)    
    node_f = Node("f", node_e)   # e -> d -> c -> b -> a -> None
    print_node(node_f)    
    node_g = Node("g", node_f)   # f -> e -> d -> c -> b -> a -> None
    print_node(node_g)
    print(node_g)
    print(length(node_g))
    print(length2(node_g))

    print()
    sequence = Node(1, Node(2, Node(3)))
    print(sequence)
    print(sequence.length())

    print()
    sequence = Node(6)
    print(sequence)
    sequence = Node(13, sequence)
    print(sequence)
    sequence = Node(11, sequence)
    print(sequence)
    sequence = Node(7, sequence)
    print(sequence)
    sequence = Node(5, sequence)
    print(sequence)
    print(sequence.length())
    print(6 + 13 + 11 + 7 + 5)
    print(recursive_sum(sequence))
    
if __name__ == "__main__":
    main()