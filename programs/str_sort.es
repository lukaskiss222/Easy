def printarr:void(arr:str*, n:int){
    printf("[")
    for i:int from 0 to n by 1 {
        printf("%s, ", arr[i])
    }
    printf("]\n")
}


def swap:void(arr:str*, i:int, j:int){
    temp:str = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
}

def b_sort:void(arr:str*, n:int){
    #bubble sort

    for i:int from 0 to (n-1) by 1{
        for j:int from 0 to (n - i - 1) by 1 {
            if arr[j] > arr[j+1] {
                swap(arr, j, j+1)    
            }
        }
    }
    
}


def merge:void(arr:str*,l:int, m:int, r:int){

    n1:int = m - l + 1
    n2:int = r - m
    #create temp arrays
    L:str(n1)
    R:str(n2)

    for i:int from 0 to n1 by 1 {
        L[i] = arr[l + i]
    }
    for j:int from 0 to n2 by 1 {
        R[j] = arr[m + 1 +j]
    }

    i:int = 0
    j:int = 0
    k:int = l

    while (i < n1) && (j < n2) {
        if L[i] <= R[j] {
            arr[k] = L[i]
            i = i + 1
        }
        else {
            arr[k] = R[j]
            j = j + 1
        }
        k = k + 1
    
    }

    while i < n1 {
        arr[k] = L[i]
        i = i + 1
        k = k + 1
    }

    # Copy the remaining
    while j < n2 {
        arr[k] = R[j]
        j = j + 1
        k = k + 1
    }
    del L
    del R

}


def mergeSort:void(arr:str*, l:int, r:int){
    if l < r {
        m:int = l + ((r-l)/2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)

        merge(arr, l, m, r)
    }
}

def main:void()
{
    n:int = readint()

    arr:str(n)
    
    for i:int from 0 to n by 1 {
        temp:char(200)
        scanf("%s", temp)
        arr[i] = temp
        }
    printf("Sorting: ")
    printarr(arr, n)
    #b_sort(arr, n )
    mergeSort(arr,0,n - 1)
    printf("===========SORTED OUTPUT=================\n")
    printarr(arr,n)
    for i:int from 0 to n by 1{
        del arr[i]
        }
    del arr

}
