
def mergesort(arr,start,end):
    if(len(arr)>1):
        mid = (start+end)//2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L,0,mid)
        mergesort(R,mid+1,end)
        n1 = len(L)
        n2 = len(R)
        i = j = k = 0
        while(i<n1 and j<n2):
            if(L[i]<=R[j]):
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while(i<n1):
            arr[k] = L[i]
            k+=1
            i+=1
        while(j<n2):
            arr[k] = R[j]
            k+=1
            j+=1

arr = [10,5,2,0,7,6,4,3]
start = 0
end = len(arr) - 1
mergesort(arr,start,end)
print(arr)
