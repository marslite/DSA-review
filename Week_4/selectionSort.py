def selectionSort(arr):
    for i in range(len(arr)):
        min_num = arr[i]
        swap_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_num:
                min_num = arr[j]
                swap_index = j
        arr[i], arr[swap_index] =  arr[swap_index], arr[i]
    # return arr






if __name__ == '__main__':
    arr = [10,4,5,3,2,1,8,9,7,0,6]
    selectionSort(arr)  
    print(arr)