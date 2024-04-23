# from collections import Deque
from __future__ import annotations


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
          #This should be returning return shortest_path,len(shortest_path)*k
          return  shortest_path
        q.append((neighbor, path+[neighbor]))
        print("Test result", path)
  #This should be returning return path, len(path) * k
  return -1

'''
Given a list of course prerequisites each in the form [0, 1] 
where 0 is a prerequisite of 1 and n, the total number of courses, 
write a function to output a valid course ordering, 
or None if not possible. Courses are numbered from 0 to n-1.
'''
def find_valid_course_ordering_if_exists(prerequisites: list[list[int]], n: int) -> list[int] | None:

  graph = to_adjacency_list(prerequisites)
  print(prerequisites, "<- Prereq")
  print(n, "<- n")
  print(graph)
  adj = [ [] for _ in range(n) ]
  indegree = [0] * n

  for pre, course in prerequisites:
    adj[pre].append(course)
    indegree[course] += 1
  
  sources = [i for i in range(n) if indegree[i] == 0  ]

  sorted_order = []
  while sources:
    vertex = sources.pop(0)
    sorted_order.append(vertex)
    for child in adj[vertex]:
      indegree[child] -= 1
      if indegree[child] == 0:
        sources.append(child)
  print("Result", sorted_order)

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
  pass