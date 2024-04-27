# from collections import Deque
from __future__ import annotations
import heapq


'''
Given a DAG that is represented as a collection of edges, i.e. ["n1", "n2"] means that n1 precedes n2 (visually, n1 -> n2),
'''

'''
Create an adjacency list for it.
'''
def to_adjacency_list(edges: list[list[str]]) -> dict[str, list[str]]:
  adj_map = {}
  # print(edges, "Edges for reference")
  # vertices = set()
  # for edge in edges:
  #   vertices.add(edge[0])
  #   vertices.add(edge[1])
  
  # for source in vertices:
  #   adj_map[source] = []
  
  # print(adj_map, "<-- CT")

  # for source,target in edges:
  #   if source in adj_map:
  #     adj_map[source].append(target)
  #   else:
  #     adj_map[source] = [target]

  #   # adj_map[source].append(target)
  

  # print(adj_map, "<-- Adj List")

  for edge in edges:
    if edge[0] not in adj_map:
      adj_map[edge[0]] = []
      adj_map[edge[1]] = []
    adj_map[edge[0]].append(edge[1])


  print( adj_map ,"<--- Adj Map")





  return adj_map




'''
Create an adjacency matrix for it where each 
respective cell contains 0 for unconnected and 1 for connected.
Index 0 represents "v1" and so on. 
'''
def to_adjacency_matrix(edges: list[list[str]]) -> list[list[int]]:
  sol = []
  vertices = set()
  for edge in edges:
    vertices.add(edge[0])
    vertices.add(edge[1])
    print(edge, "Check here")
  print(vertices, "Check here")

  n = len(vertices)

  matrix = [ n * [0] for _ in range(n) ]
  vertex_map = {}
  for idx,vertex  in enumerate(sorted(vertices)):
    vertex_map[vertex] = idx

  for edge in edges:
    x = vertex_map[edge[0]]
    y = vertex_map[edge[1]]
    matrix[x][y] = 1


  print(matrix, "Matrix")
  return matrix


'''
Suppose you’re given a list of graph edges where 
each edge is of the form ["e1", "e2"], meaning that 
"e1" is connected to "e2". You’re also given a source 
node s and destination node d.
'''

'''
Write an algorithm to return the distance of one of the shortest paths, 
where each connection costs 1 to traverse. Return -1 if there is no path.
'''
def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
  print(edges, "<-- Edges")
  print(s, "<---")
  print(d, "<---")
  visited_nodes = set()

  nodes_to_visit = []
  graph = to_adjacency_list(edges)
  print(graph, "Printed Graph")

  #We now append the first node to the visited_nodes
  nodes_to_visit.append((s,0))
  while nodes_to_visit:
    current_node, distance = nodes_to_visit.pop(0)
    # current_node[1] +=1 
    if current_node is d:
      print("Check current node: ",current_node, "Check distance: ", distance )
      return distance
    visited_nodes.add(current_node)
    for neighbor in graph[current_node]:
      if neighbor not in visited_nodes:
        nodes_to_visit.append((neighbor, distance+1))
    
  return -1





'''
Modify the above algorithm to return the path itself. 
For the test inputs, the path will always exist.
'''
def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
  print(edges, "<-- Edges CW")
  print(s, "<-- CW")
  print(d, "<-- CW")
  visited_nodes = set()
  graph = to_adjacency_list(edges)
  q = [(s, [s])]

  while q:
    (current_node, path) = q.pop(0)
    if current_node not in visited_nodes:
      visited_nodes.add(current_node)
      for neighbor in graph[current_node]:
        if neighbor == d:
          print("Path", path, "neighbor:", neighbor)
          return path + [neighbor]
        print("Neighbor", neighbor,"Path", path, "+", [neighbor])
        q.append((neighbor, path+[neighbor]))
        print("Test result", path)


  return path

'''
Modify the above algorithm to work if each connection costs k where k > 0.
'''
def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
  graph = to_adjacency_list(edges)
  print("Check here --:", graph)
  visited_nodes = set()
  q = [(s,[s])]

  while q:
    (current_node, path) = q.pop(0)
    if current_node not in visited_nodes:
      visited_nodes.add(current_node)
      for neighbor in graph[current_node]:
        if neighbor == d:
          shortest_path = path + [neighbor]
          print("Negighbor",  neighbor, 'Path', path, "Cost", len(shortest_path) * k)
          #Should this be returning return shortest_path,len(shortest_path)*k?
          return  shortest_path
        q.append((neighbor, path+[neighbor]))
        print("Test result", path)
  #Shoudln't this be returning return path, len(path) * k?
  return -1

'''
Given a list of course prerequisites each in the form [0, 1] 
where 0 is a prerequisite of 1 and n, the total number of courses, 
write a function to output a valid course ordering, 
or None if not possible. Courses are numbered from 0 to n-1.
'''
def find_valid_course_ordering_if_exists(prerequisites: list[list[int]], n: int) -> list[int] | None:

  # graph = to_adjacency_list(prerequisites)
  # print(prerequisites, "<- Prereq")
  # print(n, "<- n")
  # print(graph)
  adj = [ [] for _ in range(n) ]
  indegree = [0] * n

  for pre, course in prerequisites:
    adj[pre].append(course)
    indegree[course] += 1
  
  # sources = [i for i in range(n) if indegree[i] == 0  ]
  sources = []
  for i in range(n):
    if indegree[i] == 0:
      sources.append(i)

  sorted_order = []
  while sources:
    course = sources.pop(0)
    sorted_order.append(course)
    for dependent in adj[course]:
      # Decreasing by -1 the depenency from the previous course when it turns to 0
      indegree[dependent] -= 1
      #If the course we have now reduced it's depenency or any course that has now 0 dependency 
      #would be pushed onto the stack so it will be processed next. That's Khan's algo in a nutshell
      if indegree[dependent] == 0:
        sources.append(dependent)
  print("Result", sorted_order)

  #Checking whether the ordering contains the same exact number of courses
  #It's suppsoed to ordering/sorting them not reducing them!
  #So if the number of courses is lesser than the original input array
  #It could only means this graph was not DAG but instead was Cyclical 
  #Khan's algo and Top Sort in general does not work on Cyclical graphs
  if len(sorted_order) == n:
    return sorted_order
  else:
    return None


  # pass

'''
Suppose you’re given a list of graph edges where each edge is of the form 
("e1", "e2", 3), meaning that "e1" is connected to "e2" and has an 
edge weight of 3. The graph is connected. Write an algorithm to print 
out the an MST of the graph.

You can assume the graph is undirected for this problem. 
If there is an edge (e1, e2, 3) in the input,
you should assume there is an equivalent edge (e2, e1, 3) as well.
'''
def output_mst(edges: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
  eds = []
  adj = {}
  visited = set()

  for edge in edges:
    if edge[0] not in adj:
      adj[edge[0]]= []
    if edge[1] not in adj:
      adj[edge[1]] = []
    adj[edge[0]].append((edge[1],edge[2]))
    adj[edge[1]].append((edge[0],edge[2]))


  mst = []
  initial = next(iter(adj))
  visited.add(initial)
  min_heap = []
  for neighbor, weight, in adj[initial]:
    heapq.heappush(min_heap, (weight, initial, neighbor))
  
  #Now it's Prim's time
  while min_heap and len(mst) < len(adj)-1:
    weight,start,end = heapq.heappop(min_heap)
    if end not in visited:
      visited.add(end)
      start,end = sorted([start,end])
      mst.append((start,end,weight))

      for next_end, next_weight in adj[end]:
        if next_end not in visited:
          heapq.heappush(min_heap, (next_weight, end, next_end))

    

  print("Final result", mst)



  print("Check initial", initial)
  print("Check Heap",min_heap)
  print("Check visited",visited)
  print("Is it len(mst) == len(adj) -1?", "Yes" if len(mst) == len(adj)-1 else 'No')
  print("Adj lenght", len(adj) )
  print("MST lenght", len(mst) )


  return mst