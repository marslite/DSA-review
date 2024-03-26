
def insertionSort(arr):
    num_swaps = 0
    #Timecomplexity: O(n)
    for i in range(1,len(arr)):
        #Time complexity: O(n * (n +1))/2 = O(n^2)
        #Runtime complexity for insertion sort is O(n^2)
        for j in range(i,0,-1):
            if(arr[j] < arr[j-1]):
                num_swaps += 1
                arr[j],arr[j-1] = arr[j-1], arr[j]
                print(arr, "indext at", i)
            else:
                break
    return arr, num_swaps









if __name__ == "__main__":
    arr1 =  [1,2,3,4,5,6,7,8,9,10]
    arr2 =  [10,9,8,7,6,5,4,3,2,1]
    arr3 = [3, 8, 2, 15, 27, 21, 17, 10, 16, 7, 24, 0, 4, 6, 18, 5]

    # print(insertionSort(arr1))
    print(insertionSort(arr3))