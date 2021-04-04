
first_arr = [1,3,5,4,6,13,10,9,8,15,17]
insert_arr = [1,3,5,4,6,13,10,9,8,15]
def order(arr):
    last_leaf = int(len(arr)/2)-1
    for i in range(last_leaf,-1,-1):
        arr = swap(arr,i,last_leaf)
        #print('done with swap:',abs(i-last_leaf-1))
    print('arr:',arr)

def swap(arr,n,lastLeafInd):
    #print('check:',arr[n])
    if  2*n+2<len(arr) and arr[2*n+2]>arr[2*n+1] and arr[2*n+2]>arr[n]:
        #print('swapped:',arr[n],' and ',arr[2*n+2])
        temp = arr[n]
        arr[n] = arr[2*n+2]
        arr[2*n+2] = temp
        return swap(arr,2*n+2,lastLeafInd)
    elif 2*n+1< len(arr) and arr[2*n+1]>arr[n]:
        #print('swapped:',arr[n],' and ',arr[2*n+1])
        temp = arr[n]
        arr[n] = arr[2*n+1]
        arr[2*n+1] = temp
        return swap(arr,2*n+1,lastLeafInd)
    else:
        return arr
def insert_swap(arr,n,lastLeafInd):
    if  2*n+2<len(arr) and arr[2*n+2]>arr[2*n+1] and arr[2*n+2]>arr[n]:
        temp = arr[n]
        arr[n] = arr[2*n+2]
        arr[2*n+2] = temp
        if n != 0:
            return insert_swap(arr,int((n-1)/2),lastLeafInd)
    elif 2*n+1< len(arr) and arr[2*n+1]>arr[n]:
        temp = arr[n]
        arr[n] = arr[2*n+1]
        arr[2*n+1] = temp
        if n!= 0:
            return insert_swap(arr,int((n-1)/2),lastLeafInd)
    else:
        return arr
def insert(arr,num):
    arr.append(num)
    last_leaf = int(len(arr)/2)-1
    insert_swap(arr,last_leaf,last_leaf)
    print('arr:',arr)

def merge_sort(arr):
    size = len(arr)
    if size>2:
        L = merge_sort(arr[:size//2])
        R = merge_sort(arr[size//2:])
        indexL = 0
        indexR = 0
        while indexL+indexR != size:
            if indexL == len(L):
                arr[indexL+indexR] = R[indexR]
                indexR += 1
            elif indexR == len(R):
                arr[indexL+indexR] = L[indexL]
                indexL += 1
            elif L[indexL] > R[indexR]:
                arr[indexL+indexR] = R[indexR]
                indexR += 1
            else:
                arr[indexL+indexR] = L[indexL]
                indexL += 1
        return arr           
    elif size == 1:
        return arr
    elif arr[0] > arr[1]:
        temp = arr[1]
        arr[1] = arr[0]
        arr[0] = temp
        return arr
    else:
        return arr
'''
order(insert_arr)
insert(insert_arr,17)
order(arr)
'''
print('arr:',merge_sort(first_arr))
