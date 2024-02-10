from __future__ import annotations

'''
Tour class which is a collection of ordered points.
The functions allow you to insert points in a way that will 
keep the distance of the tour as small as possible.
Each Tour object should be able to print out the points in order, 
count its number of points, compute its total distance, 
and insert a new point using either of the two heuristics. 
The constructor creates an empty tour.
'''

from point import Point

# Hint: You will want to use a classic LinkedList Node to implement the tour.
class Node:
    def __init__(self, point):
        # This node's point 
        self.point = point

        # The next node
        self.next = None 

class Tour:
    # Creates an empty tour
    # Initialize any instance variables you think are needed.
    def __init__(self):   
        self.head = None
        self._size = 0

    # Returns string representation of the Tour.
    # Should output a list of all points on the Tour.
    def __str__(self):
      if self.head is None:
        return "Tour is currently empty"

      output = ""
      current = self.head
      #Remove extra "->" at the end (tail)
      while(current is not None):
        output += str(current.point) + "->"
        current = current.next
      return output

    # return the number of points on tour
    # Hint: You should not have to iterate through the entire Tour to get the size.
    def size(self):
      return self._size

    # Computers and returns the distance of entire tour
    def distance(self):
        if self.head is None:
          return 0

        current = self.head
        total = 0
        dist = 0
        while(current.next is not None):
          total += current.point.distance_to(current.next.point)
          current = current.next
        total += current.point.distance_to(self.head.point)
        return total

    # Helper function to insert a new point p into the Tour after a previous Node prev.
    # Example if the tour is a -> b -> c -> d
    # And you call _insert_at(p, c). Then the Tour should look like.
    # a -> b -> c -> p -> d
    # You can use this helper function in the insertNearest and insertSmallest
    # once you find the point you should insert p after.
    def _insert_at(self, p, prev: Node):
        new_node = Node(p)
        if prev is None:
          new_node.next = self.head
          self.head = new_node
        else:
          new_node.next = prev.next
          prev.next = new_node
        self._size +=1



    # Insert a new Point p to the Tour using neearest neighbor heuristic
    def insert_nearest(self, p):
      new_node = Node(p)
      if self.head is None:
        self.head = new_node
        self._size += 1
      else:
        current = self.head
        min_dist = float('inf')
        nearest_node = current

        while(current is not None):
          distance = current.point.distance_to(p)
          # print(f"distance = {distance}")
          if(distance < min_dist):
            # print(f"distance {distance} < min_dist {min_dist}")
            min_dist = distance
            nearest_node = current
          
          # prev_node = current
          current = current.next

        self._insert_at(p, nearest_node)

        




    # Insert a new Point p to the Tour using smallest increase heuristic
    def insert_smallest(self, p):
      new_node = Node(p) 
      smallest_node = None
      #Check if the head exists
      #If it exists then do this as an
      #Otherwise create a new head with Node(p)     
      if(self.head is None):
        self.head = new_node
        self._size += 1
      #I also added this one in case self.head is the only node and assign it to the smallest_node
      elif(self.head.next is None):
        self._insert_at(p, self.head)
      else:
        current = self.head
        min_dist = float('inf')
        smallest_node = None
        # original_dist = int(current.point.distance_to(p))
        # smallest_node = None
        #finding distance between p1 -> to p -> p2
        #The difference beteween p1->p->p2 - p1-> p2
 
        while(current.next is not None):
          current_point = current.point
          next_point = current.next.point
          distance_to_current_point = current_point.distance_to(p)
          distance_to_next = p.distance_to(next_point)
          current_point_distance_to_next = current_point.distance_to(next_point)
          distanceDifference = (distance_to_current_point + distance_to_next) - current_point_distance_to_next

          if(distanceDifference < min_dist):
            min_dist =  distanceDifference
            smallest_node = current

          current = current.next
        #Tail->p->head - tail-> head

        # if(self.head is not None and self.head.point is not None):
        #   distanceFour = current.point.distance_to(p)
        #   distancepH = p.distance_to(self.head.point)

        distanceFromCurrent_to_Last = current.point.distance_to(p)
        distanceFromPtoHead = p.distance_to(self.head.point)
        distanceFromCurrent_to_Head = current.point.distance_to(self.head.point)
        last_point_distance = (distanceFromCurrent_to_Last + distanceFromCurrent_to_Head) - distanceFromCurrent_to_Head
        # #Do the edge cases
        # #Adding p at the very tail
        # p1 = self.head.point
        # p2 = self.head.next.point
        # ttp = current.point.distance_to(p) 
        # pth= p.distance_to(self.head)
        # #self.head is NOT a  point object
        # tth = current.point.distance_to(self.head.point)
        # # ttpTpth = p1.distance_to(p2)
        # # difference = (distanceFour + distancepH) - p1t2
        # difference = ((ttp + pth) - tth)

        # if(difference < min_dist):
        #   mind_dist = difference
        #   smallest_node = current

        if last_point_distance < min_dist:
          minDist = last_point_distance
          smallest_node = current
        
        self._insert_at(p, smallest_node)
        # self._size += 1