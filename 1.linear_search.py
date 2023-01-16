def linear_search(arr,low,high,key):
    for i in range(low,high):
        if arr[i] == key:
            return i
    return -1
    
arr = [3,4,5,2,1,0,23,56,22,19,6,7,20,10,8]
low = 0
high = len(arr)
key = 19

print("INDEX location of the given key is: ",linear_search(arr,low,high,key))
