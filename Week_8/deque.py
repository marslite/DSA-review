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
        pass

    def removeFirst(self,val):
        pass

    def asList(self):
        pass


if __name__ == "__main__":
    print("Working with Deque")