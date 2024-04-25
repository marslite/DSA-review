from __future__ import annotations
import heapq

'''
Complete the StreamHandlerKLargest class that has a capacity k by filling in the methods.
'''

class StreamHandlerKLargest:
  def __init__(self, k: int) -> None:
    self.k = k
    self.pq = []
  
  '''
  This method adds the stream element to the collection. 
  You only need to store the k largest elements seen so far at any given point in time.
  '''
  def add_stream_element(self, e: int) -> None: 
    print(e, "<---")
    if len(self.pq) < self.k:
      heapq.heappush(self.pq, e)
    else:
      if self.pq[0] < e:
        heapq.heappop(self.pq)
        heapq.heappush(self.pq,e)
      # heapq.heappushpop(self.pq, max(self.pq[0], e))
    print(self.pq, "<---- Check here")
    # pass




  ''' 
  This method returns the k largest elements seen so far.
  '''
  def k_largest(self) -> list[int]: 
    print("Visualize whole heap ->",self.pq)
    return self.pq

'''
Complete the StreamHandlerKSmallest class that has a capacity k by filling in the methods.
'''

class StreamHandlerKSmallest:
  def __init__(self, k: int) -> None:
    self.k = k
    self.pq = []
  
  '''
  This method adds the stream element to the collection. 
  You only need to store the k smallest elements seen so far at any given point in time.
  '''
  def add_stream_element(self, e: int) -> None: 
    if len(self.pq) < self.k:
      heapq.heappush(self.pq, -e)
    else:
      if -self.pq[0] >= e:
        heapq.heappop(self.pq)
        heapq.heappush(self.pq, -e)
    
    print("Max Heap ->", self.pq)



  ''' 
  This method returns the k smallest elements seen so far.
  '''
  def k_smallest(self) -> list[int]: 
    return [-i for i in self.pq]

''' 
Write a function that creates a copy of the list, and sorts it in ascending order
using a heap.
'''
def heapsort(input_list: list[int]) -> list[int]: 
  copy = [val for val in input_list]
  print("Copy: ", copy)
  # print("Heapify", heapq.heapify(copy))
  heapq.heapify(copy)

  return copy



'''
Suppose we have some data that can be expressed as a tuple (a, b, c). 
We want to get the top k tuples out of a collection of n total tuples, 
where k <= n. Each datapoint has a score, defined as 2*a + 5*b + 10*c, 
and the higher the score, the greater the datapoint. 
Complete the class for this datapoint object, and complete the below function, using a heap to do so.
'''
class Datapoint:
  def __init__(self, a: int, b: int, c: int) -> None:
    self.a = a
    self.b = b
    self.c = c

  def to_tuple(self) -> tuple[int, int, int]:
    return (self.a, self.b, self.c)
  
  def score_total(self):
    return  2*(self.a) + 5*(self.b) + 10*(self.c)

  # TODO: you may need to add additional methods here. 

# Return them as tuples, using the to_tuple method in the Datapoint class.
def get_top_k_datapoints(data_collection: list[Datapoint], k: int) -> set[tuple[int, int, int]]:
  pq = [data_collection[i] for i in range(k)]
  output = set()

  for data in data_collection[k:]:
    if data.score_total() > pq[0].score_total():
      heapq.heappop(pq)
      heapq.heappush(pq,data)
  

  for data in pq:
    output.add(data.to_tuple())
  
  print("Set Result", output)



  return output