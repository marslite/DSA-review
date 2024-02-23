#lo/   M  T                  hi
 #13, 15,17,19,1,3,5,7,9, 11
# LOW = 1


def searchRotatedArray(arr,target):
    #Runtime complexity: O(log n)
    #Space complexity: O(1)
    lo = 0
    hi = len(arr) - 1
    while(lo <= hi):
        mid = (lo + hi )// 2
        if arr[mid] == target:
            return "Target:  " + str(target) +  "  found at position " +  str(mid)
        #case1 arr[lo] > arr[mid] -> we have pivot in between
        if arr[lo] > arr[mid]:
            if target >= arr[lo] or target <= arr[mid]:
                hi = mid -1
            else:
                lo = mid + 1
        else:
            if target > arr[mid]:
                lo = mid +1
            else:
                hi = mid -1
    return "Nothing was found with the target: " + str(target)

        #case2 arr[lo] < arr[mid] -> no pivot, just perform normal binary search


def searchRotatedArraywithDuplicates(arr,target):
    #Runtime complexity: O(log n)
    #Space complexity: O(1)
    lo = 0
    hi = len(arr) - 1
    while(lo <= hi):
        mid = (lo + hi )// 2
        if arr[mid] == target:
            return "Target:  " + str(target) +  "  found at position " +  str(mid)
        
        while(lo != mid and arr[lo] == arr[mid] ):
            lo +=1
        #case1 arr[lo] > arr[mid] -> we have pivot in between
        if arr[lo] > arr[mid]:
            if target >= arr[lo] or target <= arr[mid]:
                hi = mid -1
            else:
                lo = mid + 1
        else:
            if target > arr[mid]:
                lo = mid +1
            else:
                hi = mid -1
    return "Nothing was found with the target: " + str(target)


def question3(n):
    result = n
    for i in range(1,n):
        if(i == 0):
            return result
        else:
            result *= i
    
    return result

def question4(n):
    result = n
    for i in range(1,n):
        result *= i
    
    return result
    
def question5(n):
    if( n == 1):
        return 1
    return question5(n-1) * n 


def sum_list_itr(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum

def sum_to_rec(lst: list):
    sum = 0
    if(len(lst) == 0):
        return 0
    else:
        return lst[0] + sum_to_rec(lst[1:])








if __name__ == '__main__':
    arr = [1,3,5,7,9,11,13,15,17,19]
    rot_arr = [13,15,17,19,1,3,5,7,9,11]
    rot_dup = [11,11,11,11,11,11,11,11,11]

    # print(question4(7))
    # {[],[],[32(2)],[43],[],[15],[16],[42],[19],[27]}

    lst = [1,2,3,1]
    print(sum_to_rec(lst))

    # print(searchRotatedArray(rot_arr,15))

    # for i in range(0,20):


        # print(searchRotatedArraywithDuplicates(rot_dup,i))