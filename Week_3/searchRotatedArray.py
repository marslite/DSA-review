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



if __name__ == '__main__':
    arr = [1,3,5,7,9,11,13,15,17,19]
    rot_arr = [13,15,17,19,1,3,5,7,9,11]
    rot_dup = [11,11,11,11,11,11,11,11,11]

    # print(searchRotatedArray(rot_arr,15))

    for i in range(0,20):
        # print(searchRotatedArray(rot_arr,i))
        # print(searchRotatedArray(arr,i))
        print(searchRotatedArraywithDuplicates(rot_dup,i))