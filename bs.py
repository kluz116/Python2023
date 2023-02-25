def buble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr
            


x = [12,3,4,1,7,6,8]
print(buble_sort(x))