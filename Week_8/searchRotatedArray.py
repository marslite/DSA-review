

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




if __name__ == "__main__":
    print("Binary Search ~ Rotated Array")
    arr = [1,3,4,5,6,8]
    print(standardBinarySearch(arr,5))