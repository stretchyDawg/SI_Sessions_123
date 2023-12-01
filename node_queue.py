
import node

class NodeQueue:
    __slots__ = ['__size', '__front', '__back']

    def __init__(self):
        self.__size = 0
        self.__front = None
        self.__back = None

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def __repr__(self):
        string = '['

        if not self.is_empty():
            string += str(self.__front.get_value())
            node = self.__front.get_next()
            while node is not None:
                string += ', ' + str(node.get_value())
                node = node.get_next()

        string += ']'
        return string

    def enqueue(self, value):
        #make a new node with the value
        new = node.Node(value)
        #if queue is empty, set front AND back to new node
        if self.is_empty():
            self.__front = new
            self.__back = new
        #else, set back.next to the new node
        else:
            self.__back.set_next(new)
        #change back to the new node
            self.__back = new
        #increment size
        self.__size += 1

    def front(self):
        if self.is_empty():
            raise IndexError('empty queue')
        else:
            return self.__front.get_value()

    def back(self):
        if self.is_empty():
            raise IndexError('empty queue')
        else:
            return self.__back.get_value()

    def dequeue(self):
        if self.is_empty():
            raise IndexError('empty queue')

        else:
            value = self.__front.get_value()
            self.__front = self.__front.get_next()
            self.__size -= 1

            if self.is_empty():    #front is None but back is not
                self.__back = None
            
            return value

def main():
    pass

if __name__ == "__main__":
    main()