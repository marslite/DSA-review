import heapq
heap = []

#This heapq.heappush(heap,item) ensures that the list is still a  heap.
# heappush() takes O(log n) time
heapq.heappush(heap,3)
heapq.heappush(heap,5)
heapq.heappush(heap,1)

print(heap);

#heappop() takes O(log n) time.
min_element = heapq.heappop(heap)
print(min_element);
min_element = heapq.heappop(heap)
print(min_element)
min_element = heapq.heappop(heap);
print(min_element);
print(heap);

#If you have tuples, it will sort by the first element and 
#use second element for ties
heap = [];
heapq.heappush(heap, (5, 'write some code'));
heapq.heappush(heap, (7, 'release product'));
heapq.heappush(heap, (1, 'write spec'));
heapq.heappush(heap, (3, 'create tests'));
heapq.heappush(heap, (1, 'write spec'));

class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age

        #Compare by name first, then by age if there's a tie
    def __lt__(self,other):
        if self.name == other.name:
            return self.age < other.age
        return self.name < other.name
    
    def __repr__(self):
        return f'Person(name={self.name}, {self.age})'
    
heap = []
heapq.heappush(heap, Person("Ann",16));
heapq.heappush(heap, Person("Bob",14));
heapq.heappush(heap, Person("Sam",12));
heapq.heappop(heap);

for i in heap:
    print(i);


# Here's how to setup a heap of fixed size. Here's an example
max_size = 20;
heap = [];
for i in range(0,100):
    if len(heap) >= 20:

        print("if ", i, ">=20", "then ->", heapq.heappushpop(heap,i))
    else:
        print("Else heappush ", i,heapq.heappush(heap, i))

print(len(heap));
print(heap);

#By using Max Heap we can multiply the values you're adding by -1
#Thus the elements you heappop will be the 'largest' after you

max_heap = []
heapq.heappush(max_heap, Person("Alice", -16))
heapq.heappush(max_heap, Person("Billy", -14))
heapq.heappush(max_heap, Person("Sam", -12))
print(heapq.heappop(max_heap));


#Dequeue 

