class Node:
    __slots__ = ["__value", "__next"]

    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

def print_node(node):
    if node is None:
        print(None)
    else:
        value = node.get_value()
        print(str(value), "-> ", end = "")   # GET RID OF END TO PRINT NICELY ON ONE LINE
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
    print(length(node_g))


if __name__ == "__main__":
    main()