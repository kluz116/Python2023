def linear_search(arr,targetValue):

    for item in arr:
        if targetValue == item:
            return f'The Target Value {targetValue} is found at position {arr.index(item)} of the lists : {arr}'


x = [20,30,40,50,60,70,80,90,100]

print(linear_search(x,70))