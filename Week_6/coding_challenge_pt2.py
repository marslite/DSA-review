from __future__ import annotations

'''
For Questions 6-8, you'll be given a recurrence relation and asked to turn it into code. 
You do not have to do it optimally. Assume that the input provided will always be nonnegative. 
'''

'''
Question 6. 
f(n) = f(n-1) + f(n-2)
f(0) = f(1) = 1
'''
def question6(n):
  if n == 0 or n == 1:
    return 1
  
  return question6(n-1) + question6(n-2)

'''
Question 7. 
f(n) = f(n-1) + f(n-2) + f(n-3)
f(0) = f(1) = f(2) = 1
'''
def question7(n):
  if n == 0 or n ==1 or n == 2:
    return 1
  return question7(n-1) + question7(n-2) + question7(n-3)


'''
Question 8. 
is_even(n) = is_odd(n-1)
is_odd(n) = is_even(n-1)
is_even(0) = True
is_odd(0) = False

Return "even" if even, "odd" if odd, but your solution must use 
the above recursive structure and helper functions is_even(n) and is_odd(n).
'''
def question8(n):

  def is_even(n):
    if n == 0:
      return True
    return is_odd(n-1)
  
  def is_odd(n):
    if n == 0:
      return False
    return is_even(n-1)

  if is_even(n):
    return "even"
  
  if is_odd(n):
    return "odd"


'''
Question 4. Write a function to traverse the tree in an breadth first search fashion,
returning a list of node values in the order the nodes were traversed.
In each level, traverse from left to right.
'''
def question4(node: TreeNode) -> list[int]:
  visited = []
  db = deque([node])
  while(db):
    curr = db.popleft()
    if curr.left:
      db.append(curr.left)
    
    if curr.right:
      db.append(curr.right)
    
    visited.add(curr.val)

return visited 