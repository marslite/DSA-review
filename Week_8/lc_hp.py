class ListNode:
    def __init__(self,key: -1, val:-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode(0,0) for i in range(1000)]

        
    def put(self, key: int, value: int) -> None:
        hashedIdx = key % len(self.map)
        cur = self.map[hashedIdx]
        while(cur.next):
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self, key: int) -> int:
        hashedIdx = key % len(self.map)
        cur = self.map[hashedIdx].next
        while(cur):
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        hashedIdx = key %  len(self.map)
        # prev = self.map[hashedIdx]
        # current = prev.next
        cur = self.map[hashedIdx]
        prev = cur.next
        while(cur and cur.next):
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


        