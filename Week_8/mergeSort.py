

def mergeSort(arr):
    divide(arr,0,len(arr)-1)



def divide(arr,lo,hi):
    #Base Cae
    if lo >= hi:
        return
    mid = (lo + hi) // 2 +1

    #Divide Bottom half
    divide(arr,lo,mid-1)

    #Divide Top Half
    divide(arr,mid, hi)

    #Merge it together
    merge(arr,lo,mid,hi)


def merge(arr,start1,start2,end2):
    p1 = start1
    p2 = start2
    cur = start1
    copy = arr[:]
    while(cur <= end2):
        if p1 < start2 and p2 <= end2:
            if copy[p1]<copy[p2]:
                arr[cur] = copy[p1] 
                p1 += 1
            else:
                arr[cur] = copy[p2]
                p2 += 1
        elif p1< start2:
            arr[cur] = copy[p1]
            p1 += 1
        else:
            arr[cur] = copy[p2]
            p2 +=1
        
        cur += 1



if __name__ == "__main__":
    arr = [8,5,3,2,1,9,7,6,4,0]
    mergeSort(arr)
    print(arr)