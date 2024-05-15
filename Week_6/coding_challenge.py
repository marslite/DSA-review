from __future__ import annotations
from treenode import TreeNode
from narytreenode import NaryTreeNode
from collections import deque

'''
Questions 1-4 use the TreeNode class in treenode.py.
The test tree looks like the following
                   1
                 /   \
                2     3
               / \   / \
              4  5  6   7

Do not use any global variables.
'''

'''
Question 1. Write a function to traverse the tree in an inorder fashion,
returning a list of node values in the order the nodes were traversed.
Traverse the left side then the right side. 
'''
def question1(node: TreeNode) -> list[int]:
  visited = []
  def traverse(curNode,visited):
    if curNode is None:
      return
    traverse(curNode.left, visited)
    visited.append(curNode.val)
    traverse(curNode.right,visited)
    return visited
  
  traverse(node,visited)
  return visited



'''
Question 2. Write a function to traverse the tree in an preorder fashion,
returning a list of node values in the order the nodes were traversed.
Traverse the left side then the right side. 
'''
def question2(node: TreeNode) -> list[int]:
  visited = []
  def traverse(curNode, visited):
    if curNode is None:
      return 
    visited.append(curNode.val)
    traverse(curNode.left,visited)
    traverse(curNode.right,visited)
    return visited
  
  traverse(node,visited)
  return visited


'''
Question 3. Write a function to traverse the tree in an postorder fashion,
returning a list of node values in the order the nodes were traversed.
Traverse the left side then the right side. 
'''
def question3(node: TreeNode) -> list[int]:
  visited = []
  def traverse(curNode,visited):
    if curNode is None:
      return 
    traverse(curNode.left,visited)
    traverse(curNode.right,visited)
    visited.append(curNode.val)
    return visited
  
  traverse(node,visited)
  return visited

'''
Question 4. Write a function to traverse the tree in an breadth first search fashion,
returning a list of node values in the order the nodes were traversed.
In each level, traverse from left to right.
'''
def question4(node: TreeNode) -> list[int]:
  visited = []
  db = deque([node])
  while db:
    curr = db.popleft()
    if curr.left and curr.left.val < curr.right.val:
      db.append(curr.left)
    if curr.right and curr.right.val > curr.left.val:
      db.append(curr.right)
    visited.append(curr.val)
  print("Check", visited)
  return visited





'''
Question 5. Write a function that returns the size of each subtree
in an n-ary tree. Return the answer as a normal dictionary, not defaultdict.

See the NaryTreeNode class in narytreenode.py for the definition.
The test tree looks like the following
                 A
               / | \
              B  C  D
                   / \
                  E   F
'''
def question5(nary_node: NaryTreeNode) -> dict[str, int]:
  visited = {}
  def dfs(node,visited): 
    if node is None:
      return
    size = 1
    for nbr in node.children:
      size += dfs(nbr,visited)
    visited[node.val] = size
    return size

  print("Result", dfs(nary_node,visited))
  print("Visited", visited)
  return visited
  # res = dfs(nary_node,visited)