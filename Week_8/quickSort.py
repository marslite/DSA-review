def quickSort(arr):
    _quickSort(arr,0,len(arr)-1)


def _quickSort(arr,lo,hi):
    if lo >= hi:
        return
    pivot = partition(arr,lo,hi)

    #Partition bottom half
    _quickSort(arr,lo,pivot-1)
    #Partition top half
    _quickSort(arr,pivot+1,hi)
    


def partition(arr,lo,hi):
    #Return the index of our pivot element
    #Everything with index < idx of pivot is < pivot
    pivot = arr[lo]
    swap_idx = lo + 1
    for i in range(lo+1, hi + 1):
        if arr[i] <pivot:
            arr[i],arr[swap_idx] = arr[swap_idx], arr[i]
            swap_idx += 1

    arr[lo], arr[swap_idx-1] = arr[swap_idx-1], arr[lo]
    return swap_idx -1







if __name__ == "__main__":
    print("Quicksort")
    arr = [10,9,44,5,3,2,4,5,6,2,1,0]
    quickSort(arr)
    print(arr)