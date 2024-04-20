class MaxPriorityQueue:
    #Create a max property queue
    def __init__(self):
        self.arr = [None]
    
    #Inserts a key into the priority queue
    def insert(self, key):
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
        pass


    #Return and remove the largest key
    def delMax(self):
        pass

    #Helper function for delete
    def sink(self):
        pass


    #Returns a boolean indicating if the priority queue is empty
    def isEmpty(self):
        return len(self.arr) == 1
    
    #Returns the number of keys in the priority queue
    def size(self):
        return len(self.arr) - 2 


def heapSort(arr):
    pq = MaxPriorityQueue()
    for item in arr:
        pq.insert(item)
    
    idx = len(arr) -1
    while(not pq.isEmpty()):
        arr[idx] = pq.delMax()
        idx -=1



if __name__ == "__main__":
    pass