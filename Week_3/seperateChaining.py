class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
          
class SeparateChainingHashMap:
    #Initialize HashMap
    def __init__(self, capacity):
         #List comprhension 
         #O(capacity) Runtime
         #O(capacity) space
         self.map = [Node("dummyKey", "dummyValue") for _ in range(capacity)]
        
    #Returns index that key is stored
    def hashedIndex(self,key):
        #Runtime O(1)
        #Space O(1)
        return key % len(self.map)

    #Adds on item to the hash map, uses seperate chaining for collisions
    def put(self, key, val):
     #O(N)/capacity (In good case scenarios) Runtime Complexity
     # O(1) Space Complexity
     idx = self.hashedIndex(key)
     cur = self.map[idx]
     while(cur.next):
         if cur.next.key == key:
             cur.next.val = val
             return
         cur = cur.next
     cur.next = Node(key,val)


    #Finds item with given key and returns associated val
    def get(self,key):
        #O(N)/capacity Runtime Complexity
        #O(1) Space Complexity
        idx = self.hashedIndex(key)
        cur = self.map[idx]
        while(cur.next):
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next


    #Deletes a key and its val from the hashmap
    def delete(self,key):
        #O(N)/capacity RC
        #O(1) SC
        idx = self.hashedIndex(key)
        prev = self.map[idx]
        cur = prev.next
        while(cur):
            if cur.key == key:
                prev.next = cur.next
            prev = cur
            cur = cur.next            


    #Overrides toString method for debugging
    def __str__(self):
        #O(n) Runtime complexity
        #O(n) Spacetime Complexity
        out = ""
        for idx in range(len(self.map)):
            cur = self.map[idx].next
            while(cur):
                out += str(cur.value) + " "
                cur = cur.next
            out += "\n"
        return out
    


if __name__ == '__main__':
    #Test cases
    map = SeparateChainingHashMap(3)
    for i in range(10):
        map.put(i, i*2)

    print(map)
     #1
     #2   

    print("Get map.get(4): ", map.get(4))
    print("Get map.get(5): ", map.get(5))
    print("Get map.get(6): ", map.get(6))
    print("Get map.get(9): ", map.get(9))
    for i in range(3):
        map.delete(i)

    print(map)





