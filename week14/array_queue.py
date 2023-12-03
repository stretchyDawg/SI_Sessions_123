import arrays
#cp unit06--/arrays.py unit12--

class Queue:
    __slots__ = ['__size', '__front', '__back', '__array']

    def __init__(self):
        self.__size = 0
        self.__front = 0
        self.__back = 0
        self.__array = arrays.Array(100)

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def __repr__(self):
        string = '['
        if not self.is_empty():
            string += str(self.__array[self.__front])
            for i in range(1, self.__size):
                index = (i+ self.__front) % len(self.__array)
                value = self.__array[index]
                string += ', ' + str(value)

        string += ']'
        return string

    def enqueue(self, value):
        #put the balue in the array at the back index
        #increment the back index and wrap it if needed

        if self.__size == len(self.__array):
            raise IndexError('queue is full.')

        self.__array[self.__back] = value
        self.__back = (self.__back + 1) % len(self.__array)
        #uses wacky math to wrap the back index to one if passes the length of array
        self.__size += 1

    def front(self):
        if self.is_empty():
            raise IndexError('empty queue')
        return self.__array[self.__front]

    def back(self):
        if self.is_empty():
            raise IndexError('empty queue')

        index = self.__back - 1
        if index < 0:
            index = len(self.__array) - 1
            """ back points at next open spot in queue, so to get the value at the end we need to increment it back"""
        return self.__array[index]

    def dequeue(self):
        if self.is_empty():
            raise IndexError('empty queue')

        #save the value at front in a variable
        #set the value at front to None
        #increment front (and wrap if needed)
        #return the value

        store_front = self.__array[self.__front]
        self.__array[self.__front] = None
        self.__front += 1

        if self.__front == len(self.__array):
            self.__front = 0
            #alternative to that wacky math

        self.__size -= 1
        
        return store_front
    