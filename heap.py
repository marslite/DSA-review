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