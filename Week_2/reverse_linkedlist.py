class Node:
    def __init__(self, item, next= None):
        self.item = item
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = Node("dummy")
        self._size = 0

    def __str__(self):
        #O(N) Runtime
        # O(N) Space
        out = "" 
        cur = self.head.next
        while (cur is not None):
            out += str(cur.item) + "~"
            cur = cur.next
        return out
    

    def insertFront(self, item):
        #O(1) Runtime
        #O(1) Space
        next = self.head.next
        self.head.next = Node(item)
        self.head.next.next = next 
        self._size += 1

    def insertLast(self, item):
        #O(N) Runtime
        #O(1) Space
        cur = self.head
        while(cur.next is not None):
            cur = cur.next
        cur.next = Node(item)
        self._size += 1

    def removeBeginning(self):
        #O(1)Runtime 
        #O(1) space

        assert(self.size() > 0)
        #H ->1 -> 2
        #Result after removing 
        # H->2
        self.head.next = self.head.next.next
        self._size -= 1

    def size(self):
        #O(1)Runtime 
        #O(1) space
        return self._size
    

    def reverseLinkedList(self):
        curr = self.head.next
        prev = None
        
        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next

        self.head.next = prev



if __name__ == '__main__':
    #test cases

    # testLink = LinkedList()
    # print(testLink.head.item)

    # linkedList = LinkedList()
    # for i in range(1,6):
    #     linkedList.insertFront(i)
    # print(linkedList)

    # linkedList.removeBeginning()
    # linkedList.removeBeginning()
    # ##should print 3,4,5
    # print(linkedList)

    # for i in range(6,11):
    #     linkedList.insertLast(i)
    
    # print(linkedList)
    # #shoudl print 3,4,5,6,7,8,9,10

    # lst = LinkedList()
    # for i in range(10):
    #     lst.insertFront(i)
        
    # print(lst)

    # lst.reverseLinkedList()
    # print(lst)


    linked = LinkedList()
    print(linked)
    linked.reverseLinkedList()
    print(linked)

    linked.insertFront(1)
    print(linked)
    linked.reverseLinkedList()
    print(linked)
