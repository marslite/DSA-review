
from __future__ import annotations


class Node:
  def __init__(self, val: int, next_node: Node) -> None:
    self.val = val
    self.next_node = next_node 
    
    
def insert_front(head: Node, val: int) -> Node:
  new_h = Node(val,head)
  return new_h.val


#   head.next_node.next_node = next

'''
Write a function that returns a string representation of the list.
Format-wise, for an input Node(1, Node(2, Node(3, None))) you must return
1 -> 2 -> 3
'''
def str_list(head: Node) -> str:
  output = ""
  current = head
  while(current is not None):
    output +=  str(current.val)
    if(current.next_node is not None):
      output += "->"
    current = current.next_node 
  return output

'''
Write a function that inserts to the end of a linked list and returns the head.
'''
def insert_end(head: Node, val: int) -> Node:
#   if(head is None):
#     return Node(val, None)

  current = head
  while(current.next_node is not None):
    current = current.next_node
  current.next_node = Node(val, None)
  return head

#Write a function that returns the size of the linked list
def get_size(head: Node) -> int:
  output = 0
  current = head
  while(current is not None):
    output +=1
    current = current.next_node
  return output
  

#Write a function that determines if a linked list has a cycle, given the head of the list.

def has_cycle(head: Node) -> bool:
  slow = head
  fast = head

  while(fast.next_node is not None):
    slow = slow.next_node
    fast = fast.next_node.next_node
    if(slow == fast ):
      return True    
  return False

'''
Given the head of a circular linked list, write a method to sum all elements of the list up. 
Assume all the values of the node are integers.
'''
def get_circular_list_sum(head: Node) -> int:
  output = 0
  current = head


  while(True):
    output += current.val
    current = current.next_node


    if(current == head):
      return output
  return output
    







if __name__ == '__main__':
   
   l1_head = Node(1, Node(2, Node(3, None)))
   l2_head = Node(1, Node(2, Node(3, None)))
   new_l2_head = insert_front(l2_head, 0)
   l3_head = Node(1, Node(2, Node(3, None)))
   new_l3_head = insert_end(l3_head, 4) 
   l4_head = Node(1, None)
   last_node_of_l5 = Node(3, None)
   l5_head = Node(1, Node(2, last_node_of_l5))
   last_node_of_l5.next_node = l5_head



#    print(str_list(l1_head));
  #  print(str_list(new_l3_head));
  #  print(get_size(l3_head));
  #  print(has_cycle(l1_head));
  #  print(has_cycle(l5_head));
   print(get_circular_list_sum(l5_head));
#    print(new_l2_head)