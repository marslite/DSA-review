def binarySearch(nums,target):

    if len(nums)== 0:
        return -1
    
    lo,hi =0,len(nums)-1
    while(lo <= hi):
        mid = (lo+hi) //2
        if nums[mid] == target:
            print(mid ," <-- That's the position")
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    
    #End Condition: lo > hi 
    return -1



if __name__ == "__main__":
    lst = [0,1,2,3,4,5]
    print(binarySearch(lst,3))

