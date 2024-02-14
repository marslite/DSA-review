class ListNode:

    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

#H   T
#3 1 2
        


class Deque:
    #Initialize Deque
    #RC: O(1)
    #SC: O(1)
    def __init__(self):
        self.size = 0
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    #Returning True if empty False is if it's not
    def isEmpty(self):
        return self.getSize() == 0
    
    #Return number of items in the Deque
    def getSize(self):
        return self.size

    #Inserts item to the front of the Deque
    def addFirst(self,item):
        #RC: O(1)
        #SC: O(1)

        #head <-> tail
        #head <-> 1 <-> tail
        #head <-> item <-> 1 <-> tail
        new_node = ListNode(item)
        prev_first = self.head.next
        #Update head.next.prev before we lose access to it
        self.head.next.prev = new_node
        #Update head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = prev_first
        self.size += 1



    #Inserts item at the end of the Deuque
    def addLast(self,item):
        #RC: O(1)
        #SC: O(1)
        
        #head <-> tail
        #head <-> 1 <-> tail
        #head <-> 1 <-> 2 <-> tail

        new_node = ListNode(item)
        prev_last = self.tail.prev
        #Update tail.prev.next
        self.tail.prev.next = new_node
        #Update tail.prev
        self.tail.prev = new_node
        #Update new nodes next and prev
        new_node.next = self.tail
        new_node.prev = prev_last
        self.size += 1


    #Delete and return the key-value pair at the front of the Deque
    def removeFirst(self):
        #RC: O(1)
        #SC: O(1)
        

        # head <-> 1 <-> 2 <-> tail
        #removeFirst()
        # head <-> 2 <-> tail

        #But we first let'e ensure that the  Deque does not look like this: Head <-> Tail,
        #Beucase if that's the case we  cannot remove anything 
        # current = self.head
        # if(current.next == self.tail):
        #     return False

        if self.isEmpty():
            print("Trying removing from empty list")
            return False
        
        #Always remember to update head.next.prev BEFORE updating head.next
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
    
    

    #Delete and return the key-value at the end of the deque
    def removeLast(self):
        #RC: O(1)
        #SC: O(1)
        

        # head <-> 1 <-> 2 <-> tail
        #removeLast()
        # head <-> 1 <-> tail

        if self.isEmpty():
            print("Trying removing from empty list")
            return False
        
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -=1


    #Return type: List
    # Construct a list holding all of the items in the deque from front to end and returns it
    def asList(self):
        #RC: O(n)
        #SC: O(n)

        lst = []
        current = self.head.next
        while (current.next):
            lst.append(current.value)
            current = current.next
        return lst

    
if __name__ == "__main__":
    dq = Deque()
    for i in range(1,6):
        dq.addFirst(i)
    
    for i in range(6,11):
        dq.addLast(i)

    
    #5,4,3,2,1,6,7,8,9,10
    print(dq.asList())

    dq.removeFirst()
    print("Removing one element from the Front: 4")
    print(dq.asList())

    print("Removing one elemtn from the end end: 10")
    dq.removeLast()
    print(dq.asList())



