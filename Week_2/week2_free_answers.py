

def addOne(n):
    result = n +1
    return result


def binarySearch(list, target):
    low = 0
    high = len(list) -1

    while low <= high:
        mid = (low + high) // 2
        item = list[mid]
        if item == target:
            return mid
        if item > target:
            high = mid -1
        else:
            lod = mid +1
    return -1


def double(item,lst):
    count = 0
    for i in lst:
        if i == item:
            count += 1
        if count > 1:
            return True
    return False


def doubleSearch(lst):
    for i in range(0,len(lst)):
        for j in range(i+1, len(lst)-1):
            if lst[i] == lst[j]:
                return True
    return False


def sort_sub(list):
    for sub in list:
        sub.sort()
        sub.sort()
    return list



def sort_twice(list):
    list.sort()
    list.sort()
    return list


def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
def basic(n):
    res = n + 1
    return res






def func_one(nums) -> int:
    #For nums = [1,1,1,1,1] it will output 25
    #For nums = [1,2,3,4,5] it will output 75
    #The function takes the length of array nums and then uses a nested for loop where it adds all the element of 
    #list nums (5 elements) into all_nums for n(5) times. By doing so it adds 25 elements that then getts added to
    #individally to output resulting in 25.

    #Runtime: O(n^2) since it is i in range n and then j in range n. So each of this for loop is O(n) 
    #Since there are two of them we conclude that is O(n^2)
    #Space: O(n^2) Elements get added inside a nested for loop for 5 times each time n. So O(n) * O(n) = O(n^2)

    n = len(nums)
    all_nums = []
    for i in range(n):
        for j in range(n):
            print(j)
            all_nums.append(nums[j])
    output = 0
    #This also runs O(n^2) times but when we ad O(n^2 + n^2)  we get O(n^2)
    for value in all_nums:
        output += value
    return output

# print(func_one(nums2))




def func_two(nums) -> int:
    #For nums = [1,1,1,1,1] it will output 25
    #For nums = [1,2,3,4,5] it will output 75
    #The function as before  takes the length of array nums and then uses a nested for loop where it adds all the element of 
    # the list and adds the value to value whcih has a result as the sum of the elements of the list added 5 times since the nested for loop
    # will iterate 5 times, and for each iteration the nested for loop will be adding elements to value. So 5 * 5.
    #Runtime complexity is O(n^2) since it's iterating O(n) for the first loop and then O(n) times for the second for loop where then an addition will take place.
    #So O(n) * O(n) = O(n^2)
    #Space complexity: O(1) since it will be constant the space for adding each nums[j] to value
     
    n = len(nums)
    value = 0
    for i in range(n):
        for j in range(n):
            value += nums[j]
    return value




def func_three(nums) -> int:
    #For nums = [1,1,1,1,1] it will output 3
    #For nums = [1,2,3,4,5] it will output 8
    #The funcion takes as usual the length of nums and stores it to n
    #Then begins the while loop with the condition that is true untill n is greater than 0, so n>0
    #Inside the while loop the value gets added the value of the last element of nums, which is nums[n-1]
    #Then after doing this the n gets divided by 2, so it starts to shrink that is essential for eventually exiciting the while loop.
    #Eventually the value will keep adding all the elements  untill the n will be less than 0 and exiting the while loop returning value
    #Runtime Complexity: O(log n) since the value of n is getting divided by 2 in each iteration
    #Space complexity: O(1) since it is constant time for adding nums[n-1] to value and constant time to divide n by 2
    n = len(nums)
    value = 0
    while n > 0:
        value += nums[n - 1]
        n //= 2
    return value





def func_four(nums) -> int:
    #For nums = [1,1,1,1,1] it will output 10
    #For nums = [1,2,3,4,5] it will output 30
    # The function for each num in the nums list append the sum of element + elemento to double_nums
    #This happens for each num in nums.
    #Eventually th sum of all elements inside double_nums is returned
    #Runtime complexity O(N) since it is dependend on amount of elements in nums
    #Space complexity O(1), contant time for adding the two num summed together to the list
    double_nums = []
    for num in nums:
        double_nums.append(num + num)
    return sum(double_nums)




def func_five(nums) -> int:
    #For nums = [1,1,1,1,1] it will output 32
    #For nums = [1,2,3,4,5] it will output 98
    #The function starts with a for loop that takes the size of list n
    #Insise this for loop we can find a nested for loop that iterates for each time the size of the individual element of the list
    #In case of nums[i] = 1 the for loop will iterate one time by having power_sum = 2
    #This will increase the power_sum time 2 by each indiidual item of the list nums, so if it is [1,1,1,1] for every 1 the powe_sum *2 will be calculated.
    # So this can be reaad as 2^5 = 32
    #Essentially this function multiplies two and add it up to power_sum times each number, so if for instance nums[i] = 5 then we will have 2*2*2*2*2 or 2^5
    #While computing [1,2,3,4,5]  we get = 2^1 * 2^2 * 2^3 * 2^4 * 2^5 = 32767 then in the last for loop iteration we add 1 for each individual element of 32768.
    #We enventually get total = 32767 and then finally we do modulo of it, 32767 % 99 = 98
    # In essence this function raise 2 to the power of each element of the list and then adds up to power_up than then adds up to total than then is returned 
    #after calculating modulo 99
    #Runtime = O(N * N * 2^n) The N * N is for the two  nested loops and 2^n is for power_sum that multiplies 2 to the n at each iteration
    #Runtime continued = So when calculating the runtime we have O(N*N * 2^N) which translates to O(N^2 * 2^N), since 2^n is larger than n^2 the Runtime is equal to O(2^N)
    #Space complexity will be constnat because there would be a constant  amount of space that is for power_sums and total, so O(1)
    power_sum = 1
    for i in range(len(nums)):
        for j in range(nums[i]):
            power_sum *= 2

    total = 0
    for i in range(power_sum):
        total += 1
    return total % 99



def func_six(nums) -> int:
    #For nums = [1,1,1,1,1] it will output 3
    #For nums = [1,2,3,4,5] it will output 2
    # The function starts from the first element or (2nd element) of the nums list and iterates until the last element 
    # then it checks whther the item of the list a position (nums[i]) is lesser than its previous element (nums[i-1]) AND
    # IT checks also that the element at position nums[i] is greated than the element afterwards (nums[i+1]) divided by 2.
    #If the condition is met then counts goes up by 1 otherwise count is returned as it is
    #Runtime complexity O(N) for the for loop.
    #Space complexity O(1) constant since it takes the same space to add every single time if condition is met
    count = 0
    for i in range(1, len(nums)-1):
        if nums[i] < nums[i-1] * 2 and nums[i] > nums[i+1] / 2:
            count += 1
    return count
  

def func_seven(nums: list[int]):
    #For nums = [1,1,1,1,1] it will output 8
    #For nums = [1,2,3,4,5] it will output 19
    #The function as usual takes the length of the list nums that is made of integers
    # Then it creates another variable that points to N called n
    # We encounter the first while loop that will be running until n is greater than 0
   # Inside we found an iterative for loop that starts from the frist element of the list to the last element of the list
   #it adds every element of the list nums to total, after each addition n gets divide in 2 for letting the while loop condition eventually false
   # Finally total is returned
   # Runtime complexity  the for loop runs O(n) times but for each operation n gets divided by 2 by making the while loop O(log n)
   #Since the for loop runs O(n) but n gets divided by 2 it does not remain the same, and while loop eventually will run out
   #At first suggestion it might be O(n log n), altough the time complexity is greatly affected by the division of, so eventually
   # the geometric series will lead to a smaller and smaller element so the time complexity would be only O(n)
   #Space complexity: O(1) constant since the space allocated for total remans the same as long as the other for storing the updates for the value n
  N = len(nums)
  total = 0
  n = N
  while n > 0: 
      for i in range(0, n):
          total += nums[i]
      n = n // 2
  return total



def func_eight(nums: list[int]):
    #For nums = [1,1,1,1,1] it will output 7
    #For nums = [1,2,3,4,5] it will output 14
    # The function as usual takes the lenght of list of integers nums
   # then it start a while loop that has i =1, and it iterates untill i is smaller than N which is the lenght of nums
   # Inside we have an iterative for loop that starts from 0 and it ends at 1 for the first iteration, eventually i will grow more and more
   # Inside total gets updated by adding nums[j]  to total and then finally multiplying i by 2, this will allow to add more elements to total by expanding the j range
   #Runtime Complexity: Since n remains the same and it's dependend on the size of the array O(n) while for the iterative for loop is dependent on the growth of i O(n)
   # So O(n^2)
  #Space complexity:  O(1) becuase the space will be constant for adding elements to total
  N = len(nums)
  total = 0
  i = 1
  while i < N:
      for j in range(0, i):
          total += nums[j]
      i = i * 2
  return total



def func_nine(nums: list[int]):
    #For nums1 = [1,1,1,1,1] it will output 15
    #For nums2 = [1,2,3,4,5] it will output 45
    # The function as usual takes the lenght of list of integers nums
    # It has a while loop condition that will keep on running untill i is no longer smaller than N
    #Inside we have an iterative for loop that iterates from 0 to the end of the list nums
    #then every element of nums will be added to total as a sum.
    #Eventually when done i gets multiplied by 2
    #In essence it is adding three times the sum of the elements of the list beofre i gets larger than N, so for nums1 total gets 5 added three times so 15, for nums2 15 added three times so 45
    #Runtime complexity for the while loop is O(log n) because for each iteration the i gets bigger and will will make the condition of the while loop not valid despite the size of N
    #The second iterative for loop instead will looping untll N so O(N), so we have O(log n) * O(n) == O(n log n)
   # Spacetime: O(1) constnat since it is the same space allocated for total when gets updated and for i when it gets uptaded too

  N = len(nums)
  total = 0
  i = 1
  while i < N:
      for j in range(0, N):
          total += nums[j]
      i = i * 2
  return total




def func_10(arr: list[int]):
    #First the list of int is getting sorted 
    #Second it gers reversed, by starting from the last element up to the first element at index 0, we will go down by using the -1 step
    #Eventually we use the zip function to traverse both the arrays at the same time and add num+1 and num 2 at the end of the iteration we will return complements
    #Runtime: arr.sort() is O(n log n), then we have the reverse_arr which takes O(n) to reverse, and then  the for loop is dependent on the arr which can be seen as N so O(N) so overall O(N) + O(N) + O(n log n) which
    # equals to O(n log n) since it's the most consuming
    #Space complexity: O(n) sibce for the reverse_arr we do not in the worst case scenario the size of the arr to be reversed.
    arr.sort() # This line is O(n log n) runtime. 
    reverse_arr = [arr[i] for i in range(len(arr)-1, -1, -1)]
    complements = []

  	#zip just iterates through both arrays at the same time
    for num1, num2 in zip(arr, reverse_arr):
        complements.append(num1 + num2)
  	 
    return complements 




# This function has log(N) runtime
# Where N is the input integer
def helper_func(N):
	  # does something that takes log(N) runtime. 
	  # Note that if N = 1, then the runtime is O(1)
    

#input: an arbitrarily large integer N
# def func_11(N):
#     #The function uses the helper function to calculate something specific,
#     #then whathever result it is it will be iterated over the for loop in range (N) and the helper_func will be called for each invdividual item, 
#     # and then a nother nested for loop will do the same by recalling the helper function, eventually at the end of this helper funciton will be called again.
#     #Runtime: helper_func will take O(log n) but then in the first iterative for loop we have O(N) and when we add the two we have O(n log n) then we have another for loop that calls another helper func 
#     # this will mean another O(N) * O(n log n) which will result in O(n^2 log n), we will only adding O(N)s to O(log n) because despite each time helper_func is called it doesn't change the increase
#     # of complexity meanwhile the N sizing does so we will be adding the  O(n) * O(log n) for the first loop which equals to O(n log n) then another for loop of O(n) and helper func O(log n)
#     #since we already have O(log n) in terms of complexity and it won't change by more calls to it, we will only be adding the O(N) so in this case O(n) * O( n log n) == O(n^2 log n)
#     #, so overall O(n^2 log n)
      
#     helper_func()
#   	for i in range(N):
#   	    helper_func(i)
#         for j in range(N):
#               helper_func(j)
#   	    helper_func(N)
    


# Block (A)
 def fn_a(N):
    #This function first first initializes count to 0 and i=1 then the while loop runs until i is smaller than N
    #inside we have another for loop that starts from 0 to i that is 1 at first, inside it adds 1 to count for each time it runs so twice (0,1)
    #Altough, after this this i gets multiplied by 2 and the process will continue untill i is greater than N by making the while loop condition false
    #Finally count is returned 

    #The difference with the Block B can be fond in the for loop, as we can see in block A the for loop ranges from 0 to i, i gets updated at end of the for loop.
    #While for Block B the for loop rangers from 0 to N that is totally depended on N. So all the element will be considered and count+=1 will happen for all the size n len(N)
    #for each time it gets inside the for loop and then eventually updates i. The main difference is Block A for loop ranges from 0 to whathever value  'i' has, while Block B it ranges from 0 to all the size of N
    #Even more simplified, block A is the range of the foor loop is dependent on i value while for Block B is dependent on N
    count = 0
    i = 1
    while i < N:
      for j in range(0, i):
          count += 1
      i = i * 2
    return count

# Block (B):
def fn_b(N):
  count = 0
  i = 1
  while i < N:
      for j in range(0, N):
          count += 1
      i = i * 2
  return count




class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
class LinkedList:
    def __init__(self, node):
        # head references first node in chain of nodes
        self.head = node
      
      # Function1 takes a new_node ant it puts it as a new head.
      # new_node.next = self.head means that after traversing new_node we find the previous head, which now got shifterd
      #while for self.head = new_node means that now the self.head is new_node that correctly when we do new_node.next moves to the former head now second node
      #Runtime O(1)
    def function1(self, new_node):
        new_node.next = self.head
        self.head = new_node
  
    #Function 2 is first checking whether the head is none and if it is assigns new_node as  a new head
    def function2(self, new_node):
        if self.head is None:
            self.head = new_node
        return
    #In case there is already a head, it creates a pointer cur that points to head
    #it starts a while loop that keeps on going untill cur.next is empty
    #it traverse all the nodes within the linked list
    # when it reaches the last node before it gets null it now places the new_node at the end of the linked list
    #Function2 in summary, adds a node at the end of the linked list
    #Runtime O(N)   depending on how many nodes are present
        cur = self.head
        while(cur.next):
            cur = cur.next
        cur.next = new_node
    #Function 3 checks whether there is a Head and then re-assings the head value from the original value to the second node coming after the head
    def function3(self):
        if self.head:
            self.head = self.head.next
 
  	

nums1 = [1,1,1,1,1]
nums2 = [1,2,3,4,5]
nodeT = Node(10);
alpha = LinkedList(nodeT)
print(alpha)
# print(fn_a(nums1))
# print(fn_b(nums2))