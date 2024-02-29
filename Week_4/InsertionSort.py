
def insertionSort(arr):
    num_swaps = 0
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if(arr[j] < arr[j-1]):
                num_swaps += 1
                arr[j],arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr, num_swaps









if __name__ == "__main__":
    arr1 =  [1,2,3,4,5,6,7,8,9,10]
    arr2 =  [10,9,8,7,6,5,4,3,2,1]

    print(insertionSort(arr1))
    print(insertionSort(arr2))