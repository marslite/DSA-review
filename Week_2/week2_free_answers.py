

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
    n = len(nums)
    value = 0
    while n > 0:
        value += nums[n - 1]
        n //= 2
    return value



nums2 = [1,2,3,4,5]
nums1 = [1,1,1,1,1]
print(func_two(nums1))
print(func_two(nums2))