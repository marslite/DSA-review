def selectionSort(arr):
    for i in range(len(arr)): #O(n)
        min_num = arr[i]
        swap_index = i
        for j in range(i+1, len(arr)): #N-1, N-2 ... 1 O(n)
            #Runtime complexity: O(n) * O(n) = O(n^2)
            if arr[j] < min_num:
                min_num = arr[j]
                swap_index = j
        
        arr[i], arr[swap_index] =  arr[swap_index], arr[i]
        print(arr)
    # return arr






if __name__ == '__main__':
    arr = [10,4,5,3,2,1,8,9,7,0,6]
    arr1 = [3, 8, 2, 15, 27, 21, 17, 10, 16, 7, 24, 0, 4, 6, 18, 5]
    print(selectionSort(arr1))
    # print(arr)