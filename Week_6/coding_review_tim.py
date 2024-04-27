from collections import deque
import heapq
#Graph Traversals
def graph_traversal(adj_list):
  data_structure = [adj_list.items()[0]]
  visited = set()
  while data_structure:
    #Pop and evaluate from the data structure
    node = data_structure.pop()
    if node in visited:
      continue
    visited.add(node)

    #Node operation
    print(node)
    
    #Traverse neighbors
    for neighbor in adj_list[node]:
      if neighbor in visited:
        data_structure.append(neighbor)


#DFS
def DFS(adj_list):
  stack = [adj_list.items()[0]]
  visited = set()
  while stack:
    #Pop and evaluate from the data structure
    node = stack.pop()
    if node in visited:
      continue
    visited.add(node)

    #Node operation
    print(node)
   

    #Traverse neighbors
    for neighbor in adj_list[node]:
      if neighbor in visited:
        stack.append(neighbor)

#BFS
def BFS(adj_list):
  queue = deque([adj_list.items()[0]])
  visited = set()
  while queue:
    #Pop and evaluate from the data structure
    node = queue.popleft()
    if node in visited:
      continue
    visited.add(node)

    #Node operation
    print(node)

    #Traverse neighbors
    for neighbor in adj_list[node]:
      if neighbor in visited:
        queue.append(neighbor)

#DFS Recursive
def DFS_rec(adj_list):
  _DFS_rec(adj_list, set(), adj_list.items()[0])

def _DFS_rec(adj_list, visited, node):
  #Pop and evaluate from the data structur
  if node in visited:
    return
  visited.add(node)

  #Node operation
  print(node)
  
  #Traverse neighbors
  for neighbor in adj_list[node]:
    if neighbor in visited:
      _DFS_rec(adj_list, visited, neighbor)


#DFS Recursive - Post Order
def DFS_rec(adj_list):
  _DFS_rec(adj_list, set(), adj_list.items()[0])

def _DFS_rec(adj_list, visited, node):
  #Pop and evaluate from the data structur
  if node in visited:
    return
  visited.add(node)

  #Traverse neighbors
  for neighbor in adj_list[node]:
    if neighbor in visited:
      _DFS_rec(adj_list, visited, neighbor)
  
  #Node operation
  print(node)


#MST - Prim's
'''
adj_list = {
  a : [(b, 2), (c, 1)]
  b : [(a, 2, (c, 1)]
  c : [(a, 1), (b, 1)]
}
'''
def prims(adj_list):
  heap = [(0, adj_list.keys()[0], None)]
  visited = set()
  result = []
  while heap:
    #Pop and evaluate from the data structure
    weight, node, prev = heap.pop()
    if result == ( len(adj_list.keys()) - 1 ):
      break
    if node in visited:
      continue
    visited.add(node)

    #Node operation
    if prev is not None:
      if node < prev:
        result.append((node, prev, weight))
      else:
        result.append((prev, node, weight))
    
    #Traverse neighbors
    for neighbor, nei_weight in adj_list[node]:
      if neighbor in visited:
        heap.append(nei_weight, neighbor, node)

  return result
