from __future__ import annotations


'''
Reverse a string without the built in function to do so
'''
def reverse_str(s: str) -> str:
  ## Not the best implementation but it serves its purpose
  arr = []
  new_str = ""
  for i in s:
    arr.append(i)
  
  arr = arr[::-1]
  for i in arr:
    new_str += i
  
  return new_str

'''
Find the most frequent substring of length n in a string. If there’s a tie, return the alphabetically smallest.
'''
def most_freq_substring(s: str, n: int) -> str:
  subs = {}
  
  for i in range(len(s) - n + 1):
    if s[i:i+n] not in subs:
      subs[s[i:i+n]] = 1
    else:
      subs[s[i:i+n]] += 1
    

  toList = list(subs.values())
  cond= False
  
  for i in range(len(toList)-1):
    if toList[i] == toList[i+1]:
      cond = True
    else:
      cont = False
      break
    
  if(cond == True):
    game = 'Tie'
    # lst = dict(sorted(subs.items()))
    # semi = list(sorted(lst.keys()))
    # result = semi[0]
    for curr_sub in subs.keys():
      min_sub = curr_sub
      if curr_sub < min_sub:
        min_sub = curr_sub

      result = min_sub
  else:
    game = 'Not tie'
    diff = list(subs.keys())
    result = diff[0]
    

  
  # sorted_dict = dict(sorted(subs.items()))
  # first = list(sorted_dict.keys())
  # first = list(subs.keys())
  return result

'''
What is the alphabetically smallest subsequence of length n in a string? 
For example, a string “agbf” and length 2 subsequence would be “ab”. Time complexity does not need to be optimal.
'''
def smallest_subsequence(s: str, n: int) -> str:
  #My assumption will be that ord('a') > ord('b') > ord('c') by 1 each
  #Not ideal solution
  # semiP = []
  # solution = ''
  # for i in s:
  #   semiP.append(i)

  # semiP = sorted(semiP)
  # semiP = semiP[:n]
  # for i in semiP:
  #   solution += i

  # print(solution, "<-- Check here")
  # return solution

  stack = []

  for c in s:
    while stack and ord(c) < ord(stack[-1]):
      stack.pop()

    stack.append(c)

  return ''.join(stack[:n])

  # brute = map(''.join, combinatios(s,n))
  # sub = min(sub)
  # return sub


'''
Merge N sorted lists.

Do not just append them all and use .sort()
Think of the merge technique used in mergesort.

Example
Input: [[1, 5, 8], [0, 2, 10], [4, 8, 9]]
Output: [0, 1, 2, 4, 5, 8, 8, 9, 10]
'''
def merge_n_lists(lst: list[list[int]]) -> list[int]:
  uniqum = []
  # for i in range(lst -1):
  #   if lst[i][i] > lst[i+1][i]:
  #     uniqum.append(lst[i+1][i])
  #     uniqum.append(lst[i][i])
  #   else:
  #     uniqum.append(lst[i][i])
  #     uniqum.append(lst[i+1][i])
  
  # for i in uniqum:
  #   if uniqum[i] > uniqum[i+1]:
  #     uniqum[i+1], uniqum[i] = uniqum[i], uniqum[i+1]

  #Alternative method untill clarifications are made
  sorted_arr = []

  for i in lst:
    for j in i:
      uniqum.append(j)
    

  while(uniqum):
    small = min(uniqum)
    sorted_arr.append(small)
    uniqum.remove(small)

  print("Current output", sorted_arr)

  return sorted_arr




''' 
Given a list of coordinates, sort them by increasing order for X values, then decreasing order for Y values
Example
Input: [(1,1), (2,2), (2,1), (1,2)]
Output: [(1,2), (1,1), (2,2), (2,1)]
'''
def sort_tuples(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:
  print("Original input: ", lst)
  lst.sort(key=lambda x: (x[0],-x[1]))
  print("Sorted output:", lst)
  return lst






# from stencil import *

# def test_reverse_str_1():
#   assert reverse_str("abcd") == "dcba"

# def test_reverse_str_2():
#   assert reverse_str("abbd") == "dbba"

def test_most_freq_substring_1():
  assert most_freq_substring("abaa", 2) == "aa"

def test_most_freq_substring_2():
  assert most_freq_substring("eabcdeab", 3) == "eab"

# def test_smallest_subsequence_1():
#   assert smallest_subsequence("agbf", 2) == "ab"

# def test_smallest_subsequence_2():
#   assert smallest_subsequence("batman", 3) == "aan"

# def test_merge_n_lists_1():
#   assert merge_n_lists([[1, 5, 8], [0, 2, 10], [4, 8, 9]]) == [0, 1, 2, 4, 5, 8, 8, 9, 10]

# def test_merge_n_lists_2():
#   assert merge_n_lists([[1, 3], [2, 4]]) == [1, 2, 3, 4]

# def test_merge_n_lists_3():
#   assert merge_n_lists([[1, 3], [4, 6]]) == [1, 3, 4, 6]

# def test_merge_n_lists_4():
#   assert merge_n_lists([[4, 6], [1, 3]]) == [1, 3, 4, 6]

# def test_merge_n_lists_5():
#   assert merge_n_lists([[1, 3, 5]]) == [1, 3, 5]

# def test_sort_tuples_1():
#   assert sort_tuples([(1,1), (2,2), (2,1), (1,2)]) == [(1,2), (1,1), (2,2), (2,1)]

# def test_sort_tuples_2():
#   assert sort_tuples([(2,10),(1,10),(3,10)]) == [(1,10),(2,10),(3,10)]

# def test_sort_tuples_3():
#   assert sort_tuples([(10,2),(10,1),(10,3)]) == [(10,3),(10,2),(10,1)]




    


if __name__ == '__main__':
    # a = reverse_str("hello")
    # a = (most_freq_sub('eabcdeab',3))
    # a = (most_freq_sub('abaa',2))
    # print(a)
    # lst = [(1,1), (2,2), (2,1), (1,2)]

    # tc= 'batman'
    # print(smallest_subsequence(tc, 3))

    print(most_freq_substring("abaa", 2))


    print(most_freq_substring("eabcdeab", 3))

    # rd = sort_tuples(lst)
    # print(rd)
    # lst = [[1, 5, 8], [0, 2, 10], [4, 8, 9]]
    #  print(merge_n_lists(lst))
    # print(replace(st, old,new))

