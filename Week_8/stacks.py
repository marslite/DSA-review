class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:

    def __init__(self):
        self.first_item = None
        self._size = 0

    
    def __str__(self):
        cur = self.first_item
        out = ""
        while(cur):
            out += str(cur.val) + " ->"
            cur = cur.next
        
        return out

    def push(self,item):
        old_first = self.first_item
        self.first_item = Node(item)
        self.first_item.next = old_first
        self._size += 1
        # return self.first_item



    def pop(self):
        if self.isEmpty():
            return 
        
        temp = self.first_item
        self.first_item = self.first_item.next


        

    def isEmpty(self):
        return self._size <= 0
    

if __name__ == "__main__":

    print('Stack Revision')
    stack = Stack()
    for i in range(11):
        stack.push(i)

    print(stack)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)