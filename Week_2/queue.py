#Getting started with Queue

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Queue:
    #Create an empty Queue
    def __init__(self):
        self._size = 0
        self.head = Node('Dummy')
        self.tail = self.head

    #Adds an item to the queue
    def enqueue(self, item):
        self.tail.next = Node(item)
        self.tail = self.tail.next
        self._size += 1

    #Removes and returns the least recently added item
    def dequeue(self):
        pass

    #Returns a boolean indiciating whether the queue is emtpy or not
    def isEmpty(self):
        return self.size() == 0

    #Returns the numner of itmes in the queue
    def size(self):
        return self._size

    #Returns a list of items in the queue
    def items(self):
        pass