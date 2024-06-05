def selectionSort(arr):
    #Runtime: O(n) * O(n) = O(n^2)
    for i in range(len(arr)):
        min_number = arr[i]
        swap_idx = i
        for j in range(i+1,len(arr)): #O(n)
            if arr[j] < min_number:
                min_number = arr[j]
                swap_idx = j
        arr[i], arr[swap_idx] = arr[swap_idx], arr[i] #Swampping is Contant Time
    return arr







if __name__ == "__main__":
    print("Selection Sort")
    arr = [10,6,8,4,5,1,3,7,2,2,2,2,3]
    print(selectionSort(arr))
