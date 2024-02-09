#Getting started with Queue

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Queue:
    #Create an empty Queue
    #Runtime O(1) time and space
    def __init__(self):
        self._size = 0
        self.head = Node('Dummy')
        self.tail = self.head

    #Adds an item to the queue
    #Runtime O(1) time and space
    def enqueue(self, item):
        self.tail.next = Node(item)
        self.tail = self.tail.next
        self._size += 1

    #Removes and returns the least recently added item
    #Runtime O(1) space and time
    def dequeue(self):
        #O(1) Space and Time

        # [1]
        # self.head.next = None
        #self.tail = 1

        if self.isEmpty():
            print("Trying to remove from an empty queue")
            return
        out = self.head.next
        self.head.next = self.head.next.next
        self._size -= 1
        if self.isEmpty():
            self.tail = self.head
        return out.item


    #Returns a boolean indiciating whether the queue is emtpy or not
    #Runtime O(1) Space and Time
    def isEmpty(self):
        return self.size() == 0

    #Returns the numner of itmes in the queue
    #Runtime O(1) Space and Time
    def size(self):
        return self._size

    #Returns a list of items in the queue
    def items(self):
        #Runtime O(N) Time and Space  (since the iteration over n times)
        output = []
        cur = self.head.next
        while(cur):
            output.append(cur.item)
            cur = cur.next
        return output
    
    
if __name__ == '__main__':
    # queue = Queue()
    # print(queue.isEmpty())

    # for i in range(3):
    #     queue.enqueue(i)

    # print(queue.items())
    # # print(queue.isEmpty())
    # print("Removing Nodes from the Queue")
    # for _ in range(4):
    #     print(queue.dequeue())

    # for i in range(2):
    #     queue.enqueue(i)

    # print(queue.items())

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.dequeue())
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.items())