class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class Deque:
    def __init__(self):
        self.size = 0
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmtpy(self):
        return self.getSize() == 0

    def getSize(self):
        return self.size

    def addFirst(self,val):
        newNode = ListNode(val)
        prev = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = prev
        self.size += 1

    def addLast(self,val):
        newNode = ListNode(val)
        prev = self.tail.prev
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = prev


    def removeFirst(self):
        if self.isEmtpy():
            print("Cannot remove from empy list")
            return
        
        self.head.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -=1 

    def removeLast(self):
        if self.isEmtpy():
            print("Cannot remove from an empty list")
            return
        
        # prev = self.tail.prev.prev.next
        self.tail.prev.prev.next = self.tail
        self.tail.prev =  self.tail.prev.prev
        self.size -= 1



    def asList(self):
        lst = []
        cur = self.head.next
        while(cur.next):
            lst.append(cur.val)
            cur = cur.next
        return lst


if __name__ == "__main__":
    print("Working with Deque")
    dq = Deque()
    for i in range(10):
        dq.addFirst(i)
    
    print(dq.asList())
    dq.removeFirst()
    print(dq.asList())
    dq.removeLast()
    print(dq.asList())
