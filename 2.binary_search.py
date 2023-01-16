def binary_search(arr,low,high,mid,key):
    while high>=low:
        mid = (high+low)//2
        if key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
        else:
            return mid
    return -1
    
arr = [3,4,5,2,1,0,23,56,22,19,6,7,20,10,8]
low = 0
high = len(arr)-1
mid = 0
key = 19
print('original array:',arr)
arr.sort()
print('sorted array:',arr)
print("INDEX location of the given key is: ",binary_search(arr,low,high,mid,key))
