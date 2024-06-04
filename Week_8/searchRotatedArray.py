

def standardBinarySearch(arr,target):
    lo = 0
    hi = len(arr) -1
    while(lo <= hi):
        mid = (hi + lo) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            lo -=1
        elif arr[mid] < target:
            hi +=1
    return None


def searchRoratedArray(arr,target):
    lo = 0
    hi = len(arr) -1
    while(lo <= hi):
        mid = (lo + hi) //2
        if arr[mid] == target:
            return mid
        #Case 1 arr[lo] > arr[mid] -> we have pivot in between
        if  arr[lo] > arr[mid]:
            if target >= arr[lo] or target <= arr[mid]:
                hi = mid -1
            else:
                lo = mid +1
        #Case 2 arr[lo] < arr[mid] -> no pivot, just perform normal binary search
        else:
            if arr[mid] > target:
                lo -=1
            else:
                hi += 1
            #Both implementations work
            # if target > mid:
            #     lo = mid + 1
            # else:
            #     hi = mid -1
    return None







if __name__ == "__main__":
    print("Binary Search ~ Rotated Array")
    arr = [1,3,5,7,9,11,13,15,17,19]
    rot_arr = [13,15,17,19,1,3,5,7,9,11]
    print(standardBinarySearch(arr,11))
    print(searchRoratedArray(rot_arr,1))