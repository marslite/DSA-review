class Node:
    def __init__(self,item, next=None):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node('dummy')
        self._size = 0

    def __str__(self):
        out = ""
        cur = self.head.next
        while(cur):
            out += str(cur.item) +  "->"
            cur = cur.next
        return out


    def insertFront(self,item):
        next = self.head.next
        self.head.next = Node(item)
        self.head.next.next = next
        self._size +=1 



    def insertLast(self,item):
        cur = self.head
        while(cur.next):
            cur = cur.next
        cur.next = Node(item)
        self._size += 1


    def removeBeginning(self):
        assert(self.size() > 0)
        self.head.next = self.head.next.next
        self._size -=1
    
    def size(self):
        return self._size
    

    def reverseLinkedList(self):
        cur = self.head.next
        prev = None
        while(cur):
            Next = cur.next
            cur.next = prev
            prev = cur
            cur = Next
        self.head.next = prev




if __name__ == '__main__':
    print('test')
    node = Node('a')
    node1 = Node('b')
    node2 = Node('c')
    linkl = LinkedList()
    for i in range(1,6):
        linkl.insertFront(i)
    
    print(linkl)

    node = LinkedList()
    for i in range(1,6):
        node.insertFront(i)
    
    print(node)
    node.reverseLinkedList()
    print(node)



    