import node

class Stack:
    __slots__ = ["__top", "__size"]

    def __init__(self):
        self.__top = None
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__top is None

    def push(self, value):
        new_top = node.Node(value, self.__top)
        self.__top = new_top
        self.__size += 1
    
    def peek(self):
        if self.is_empty():
            raise IndexError("empty stack")
        return self.__top.get_value()

    def pop(self):
        if self.is_empty():
            raise IndexError("empty stack")
        else:    
            popped = self.__top.get_value()
            self.__top = self.__top.get_next()
            self.__size -= 1
            return popped

    def print_stack_comma(self):
        """
        Prints node stack in comma (", ") form (for who_goes_there.py __repr__ implementation for crewmate class)
        """
        string = ""
        node = self.__top
        while node is not None:
            string += str(node.get_value())
            node = node.get_next()
            if node is not None:
                string += ', '
        return string
    
    def __repr__(self):
        string = "["
        node = self.__top
        while node is not None:
            string += str(node.get_value())
            if(node.get_next() != None):
                string += ' -> '
            node = node.get_next()
        string += ']'
        return string
    
    def __len__(self):
        return self.__size
    
def main():
    stack = Stack()
    print(stack)
    stack.push(1)
    print(stack)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
    print(stack.peek())
    stack.pop()
    print(stack)
    print(stack.peek())
    print()

    print()
    stack2 = Stack()
    print(stack2)
    stack2.push(1)
    print(stack2)
    stack2.push(2)
    print(stack2)
    stack2.push(3)
    print(stack2)
    stack2.push(4)
    print(stack2)
    stack2.push(5)
    print(stack2)
    stack2.pop()
    print(stack2)
    stack2.pop()
    print(stack2)
    stack2.pop()
    print(stack2)
    stack2.pop()
    print(stack2)
    stack2.pop()
    print(stack2)
    print()

if __name__ == "__main__":
    main()
    