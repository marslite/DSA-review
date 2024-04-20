class MaxPriorityQueue:
    #Create a max property queue
    def __init__(self):
        self.arr = [None]
    
    #Inserts a key into the priority queue
    def insert(self, key):
        #Runtime O(LOG N)
        #Space O(1)
        self.arr.append(key)
        self.swim()


    #Helper function for insert
    def swim(self):
        idx = len(self.arr) -1
        while(idx//2 > 0 and self.arr[idx//2] < self.arr[idx]):
            self.arr[idx], self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
            idx = idx//2

    
    #returns the largest key
    def get_max(self):
        assert not self.isEmpty()
        return self.arr[1]


    #Return and remove the largest key
    def delMax(self):
        #Runtime O(log n)
        #Space O(1)
        assert not self.isEmpty()
        self.arr[1], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[1]
        val = self.arr.pop()
        self.sink()
        return val

    #Helper function for delete
    def sink(self):
        idx =1
        while(idx * 2 < len(self.arr)):
            cur = self.arr[idx]
            left = self.arr[idx *2]
            right = float('-inf')
            if (idx *2 +1 < len(self.arr)):
                right = self.arr[idx *2 +1]
            
            if cur >= left and cur >= right:
                return
            
            if left > right:
                self.arr[idx], self.arr[idx*2] = self.arr[idx*2], self.arr[idx]
                idx = idx *2
            else:
                self.arr[idx], self.arr[idx*2+1] = self.arr[idx*2+1], self.arr[idx]
                idx =idx*2 +1


    #Returns a boolean indicating if the priority queue is empty
    def isEmpty(self):
        return len(self.arr) == 1
    
    #Returns the number of keys in the priority queue
    def size(self):
        ##Double check why -2 and not -1
        return len(self.arr) - 2 


def heapSort(arr):
    pq = MaxPriorityQueue()
    #Runtime: O(n log n)
    #Space O(N)
    for item in arr:
        pq.insert(item)
    print(pq.size())
    
    idx = len(arr) -1
    while(not pq.isEmpty()):
        arr[idx] = pq.delMax()
        idx -=1
    #O(N log n)     + O(N log n) = O(2 N log N) = O(n log n) 
    #O(n)
    return arr




if __name__ == "__main__":
    arr = [6,10,4,3,2,7,8,9,1,5,11,12,4,5,-6]
    len(arr)
    heap = heapSort(arr) 
    print(heap)
    # print(heapSort(arr).size())