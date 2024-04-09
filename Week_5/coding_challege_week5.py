from __future__ import annotations
from treenode import TreeNode
from collections import deque

'''
Create a BT that looks like this and return the root.
         3         
       /   \        
      2     6     
    /     /   \    
   1     5     7 

For example, you your code should do the following.

root = create_BST() 
print(x.value) # Prints 3.
print(x.left.value) # Prints 2

You only need to construct the above tree and return the root of that tree.
'''

def create_BST() -> TreeNode:
  # self.val = 3
  node1 = TreeNode(1)
  node2 = TreeNode(5)
  node3 = TreeNode(7)

  node4 = TreeNode(2,node1)
  node5 = TreeNode(6, node2, node3)


  node6 = TreeNode(3,node4, node5)

  return node6
  # print(node6.value)
  # root.val = 3
  # root.left.value = 2
  # root.right.value = 6
  # root.left.left.val = 1
  # root.right.left.val = 5
  # root.right.right.val = 7

'''
Write a function to perform a preorder traversal on the BT and return the preorder as a list.
'''
def preorder_traversal(root: TreeNode) -> list[int]:
  res = []

  
  def _preorder(root):
    if root is None:
      return
    res.append(root.value)
    _preorder(root.left)
    _preorder(root.right)
    return res
  
  solution = _preorder(root)
    

  # res.append(root.value)
  # preorder_traversal(root.left)
  # preorder_traversal(root.right)

  print(solution, "Check here")
  return solution

'''
Write a function to perform an inorder traversal on the BT and return the inorder as a list. 
'''
def inorder_traversal(root: TreeNode) -> list[int]:
  res = []

  def _inorder(root):
    if root is None:
      return
    _inorder(root.left)
    res.append(root.value)
    _inorder(root.right)
    return res
  
  solution = _inorder(root)
  print(solution, "Check here")
  return solution

    

    

'''
Write a function to perform a postorder traversal on the BT and return the postorder as a list.
'''
def postorder_traversal(root: TreeNode) -> list[int]:
  res = []

  def _postorder(root):
    if root is None:
      return
    _postorder(root.left)
    _postorder(root.right)
    res.append(root.value)
    return res
  
  solution = _postorder(root)
  print("Check here", solution)
  return solution

'''
Write a function to perform a level by level order traversal on the BT.
'''

def level_order_traversal(root: TreeNode) -> list[list[int]]:
  lst = []
  q = [] 
  q.append(root)
  while len(q) > 0:
    level = []
    for i in range(len(q)):
      x = q.pop(0)
      if x is not None:
        level.append(x.value)
        q.append(x.left)
        q.append(x.right)
    lst.append(level)



    
  lst.pop()
  print(lst, "Check solution here")
  # print(lst.pop(), "Check solution here")
  
  return lst



'''
Write a function to perform a traversal where we return the k smallest elements in ascending order in this BST.
'''

def get_k_smallest_elements(root: TreeNode, k: int) -> list[int]:
  res = []

  def _inorder(root):
    if root is None:
      return
    _inorder(root.left)
    res.append(root.value)
    _inorder(root.right)
    return res
  
  solution = _inorder(root)
  print(solution[:k], "Check here")
  return solution[:k]
    

'''
Write a function to perform a traversal where we return the k largest elements in descending order in this BST.
'''

def get_k_largest_elements(root: TreeNode, k: int) -> list[int]:

  res = []

  def _inorder(root):
    if root is None:
      return
    _inorder(root.left)
    res.append(root.value)
    _inorder(root.right)
    return res

  solution = _inorder(root)
  print(solution, "Check here")
  proc = list(reversed(solution))
  print(proc, "Check here")

  return proc[:k]




'''
Complete the following Trie class.  
insert(word: str) -> None
word_exists(word: str) -> bool i.e. if our dictionary contains “doghouse”, the word “doghouse” exists but the word “dog” does not.
prefix_exists(prefix: str) -> bool i.e. if our dictionary contains “doghouse”, “dog” and “doghouse” would both be prefixes of some word(s) in our dictionary (and thus return True).
'''        
class Node:
  def __init__(self):
    self.children = {}
    self.isWord = False

class Trie:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curNode = self.root
        for i in word:
          if i not in curNode.children:
            curNode.children[i] = Node()
          else:
            pass 

          curNode = curNode.children[i]
          
        curNode.isWord = True
            
    def word_exists(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curNode = self.root

        for i in word:
          if i in curNode.children:
            curNode = curNode.children[i]
          else:
            return False
          
        print("Check here ->", curNode.isWord, word)
        return curNode.isWord
        

    def prefix_exists(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curNode = self.root
        for i in prefix:
          if i in curNode.children:
            curNode = curNode.children[i]
          else:
            return False

        return True