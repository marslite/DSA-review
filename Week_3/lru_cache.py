class Node:
    def __init__(self,key,val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key
    

class DoublyLinkedList:
    def __init__(self):
        self.back = Node("back","back")
        self.front = Node("back","back")
        self.back.next = self.front
        self.front.prev = self.back
    

    def delete(self,node):
        pass

    def addToFront(self,key,value):
        pass

    def deleteFromBack(self):
        pass

class LRU_Cache:
    def __init__(self,capacity):
        self.nodes = DoublyLinkedList()
        self.capacity = capacity
        self.inCache = {}
    
    #If node exists then delete it and add it to the front and then return the key
    def get(self,key):
        if key in self.inCache():
            val = self.inCache[key].value
            self.nodes.delete(self.inCache(key))
            self.nodes.addToFront(key,val)


    def set(key,value):
        pass


