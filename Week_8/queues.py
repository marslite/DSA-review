class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Queue:

    def __init__(self):
        self._size = 0
        self.head = Node("dummy")
        self.tail = self.head

    def enqueue(self,item):
        self.tail.next = Node(str(item))
        self.tail = self.tail.next
        self._size += 1


    def dequeue(self):
        if self.isEmpty():
            print("Trying to remove form an empty queue")
            return
        
        # if self._size == 1:
        #     self.head = None
        
        out = self.head.next.val
        
        self.head.next = self.head.next.next
        print("You removed, ", out)
        self._size -=1
        if self.isEmpty():
            self.tail = self.head

    def isEmpty(self):
        if self._size > 0:
            return False
        return True

    def size(self):
        if self.isEmpty():
            return
        
        return self._size

    def items(self):
        cur = self.head 
        out = []
        while(cur):
            out.append(cur.val)
            cur = cur.next
        return out


if __name__ == "__main__":
    print("Testing Queues")
    queue = Queue()
    queue.enqueue('hello')
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.items())
    queue.dequeue()
    queue.dequeue()
    print(queue.items())