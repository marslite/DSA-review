
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


class SeperateChaining:
    def __init__(self,capacity):
        self.map = [Node("key","value") for _ in range(capacity)]
        self.capacity = capacity



    def hashIndex(self,key):
        return key % len(self.map)

    def put(self,key,val):
        idx = self.hashIndex(key)
        cur = self.map[idx]
        while(cur.next):
            if cur.next.key == key:
                cur.next.val = val
                return
            cur = cur.next
        cur.next = Node(key,val)

    def get(self,key):
        idx = self.hashIndex(key)
        cur = self.map[idx]
        while(cur.next):
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return None


    def delete(self,key):
        idx = self.hashIndex(key)
        prev = self.map[idx]
        cur = prev.next
        while(cur):
            if cur.key == key:
                prev.next = cur
            prev = cur
            cur = cur.next



    def __str__(self):
        out = ''
        # idx = self.hashIndex(self.key)
        for idx in range(len(self.map)):
            cur = self.map[idx].next
            out += "key(" + str(cur.key) + "):  "
            while(cur):
                out += str(cur.value) + " "
                cur = cur.next
            out += "\n"
        return out
                




if __name__ == "__main__":
    print("Hashmap")
    map = SeperateChaining(3)
    for i in range(10):
        map.put(i,i*2)
    
    print(map)
    print("Get", map.get(4))