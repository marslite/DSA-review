from linkedList import LinkedList


#1->2->3
#3->2->1


# def reverseLinkedList(self):
#     cur = self.head
#     prev = None
#     while(cur):
#         Next = cur.next
#         cur.next = prev
#         prev = cur
#         cur = Next
#     return prev



if __name__ == "__main__":
    print("test")
    node = LinkedList()
    for i in range(1,6):
        node.insertFront(i)
    
    print(node)
    # reverseLinkedList(node)
    print(node)
