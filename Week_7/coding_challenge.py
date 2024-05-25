from __future__ import annotations

'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

'''
Question 1. Solve the above problem using Top Down Dynamic Programming
'''
def unique_paths_top_down(m: int, n: int) -> int:
  cache = {}

  def helper(row, col):
    if (row,col) in cache:
      return cache[(row,col)]
    
    if row == 1 and col == 1:
      return 1
    
    if row == 0 or col == 0:
      return 0

    cache[(row,col)] = helper(row-1, col) + helper(row, col-1)
    print("Cache","(",row,',',col,')', '=', "unique_td(",row-1,col,")", ",","+", "unique_td(",row-1,col,")", "=",(helper(row-1,col) + helper(row,col-1)))
    return cache[(row,col)]
  
  return helper(m,n)




# '''
# Question 2. Solve the above problem using Bottom Up Dynamic Programming
# '''
# def unique_paths_bottom_up(m: int, n: int) -> int:
#   # cache = [ [1]*n for _ in range(m)  ]
#   # print("Here's the cache",cache)
#   # for row in range(1,m):
#   #   for column in range(1,n):
#   #     cache[row][column] = cache[row-1][column] + cache[row][column-1]
  
#   # print("vis the res", cache)
#   # return cache[m-1][n-1]

#   cache = [[1] *n for _ in range(m)]
#   print(cache)
#   #Runtime O(m*n)
#   #Space O(n * m)
#   for row in range(m-2, -1,-1):
#     for column in range(n-2, -1,-1):
#       cache[row][column] = cache[row+1][column] + cache[row][column+1]
  
#   print("Cache: ",cache)
  
#   # return cache[0][0]


  '''
Question 2. Solve the above problem using Bottom Up Dynamic Programming
'''
def unique_paths_bottom_up(m: int, n: int) -> int:

  cache = [[1] *n for _ in range(m)]
  print(cache)
  #Runtime O(m*n)
  #Space O(n * m)
  for row in range(m-2, -1,-1):
    for column in range(n-2, -1,-1):
      cache[row][column] = cache[row+1][column] + cache[row][column+1]
      print(cache)
  
  print("Cache: ",cache)
  
  return cache[0][0]


def top_down_fillf(n,memo={}):
    if memo is None:
      memo = {}

    if n in memo:
      return memo[n]
    
    if n == 0:
      return 1
    
    if n ==1:
      return 1
    
    memo[n] = top_down_fillf(n-1,memo) + top_down_fillf(n-2,memo)
    print("fillf(",n,")", " =", "fillf(",n,"-","1)",top_down_fillf(n-1),"+", "fillf(",n,"-2 )", top_down_fillf(n-2), "=",top_down_fillf(n-1,memo) + top_down_fillf(n-2,memo) )

    return memo[n]

def bottom_up_fill(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  if n == 2:
    return 1
  
  dp = [0] * (n+1)
  dp[0] = 1
  dp[1] = 1
  dp[2] = 1
  for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-3]
  return dp[n]


def bottom_up_subs(n):
    if n == 0:
      return 1
    if n == 1:
      return 2
    
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
      dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[n]

def top_down_funs(n,m,memo=None):
  if memo is None:
    memo = {}
  
  if n in memo:
    return memo[n]
  
  if n==0:
    return 1
  
  memo[n] = m * top_down_funs(n-1,m,memo)
  print("memo[",n,']','=',' m', '*', " count_f(",n-1, m, memo,")", "==", memo[n])
  return memo[n]


if __name__ == "__main__":
  
#   print(unique_paths_top_down(6,6))
    # print(top_down_fillf(6, memo={}))
    # print(bottom_up_fill(3))


    # print(bottom_up_subs(4)) #Output is 8
    print(top_down_funs(3,3))
