import math

def binary_search(arr,targetItem):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = math.floor((start+end)/2)

        if targetItem == arr[middle]:
            return f'The Target Value {targetItem} is found at position {middle} of the lists : {arr}'
        if targetItem > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1


x = [20,30,40,50,60,70,80,90,100]

print(binary_search(x,20))