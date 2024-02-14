class ListNode:

    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

#H   T
#3 1 2
        


class Deque:
    #Initialize Deque
    def __init(self):
        self.size = 0
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    #Returning True if empty False is if it's not
    def is_empty(self):
        return self.getSize() == 0
    
    #Return number of items in the Deque
    def getSize(self):
        return self.size

    #Inserts item to the front of the Deque
    def addFirst(self,key,value):
        pass

    #Inserts item at the end of the Deuque
    def addLast(self,key,value):
        pass

    #Delete and return the key-value pair at the front of the Deque
    def removeFirst(self):
        pass

    #Delete and return the key-value at the end of the deque
    def removeLast(self):
        pass

    #Return type: List
    # Construct a list holding all of the items in the deque from front to end and returns it
    def asList(self):
        pass

    