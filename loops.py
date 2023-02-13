x = [20,30,40,50,60,70,80,90,100]

#Using a for loop
for i in x:
    print(i)

#Using a range method
for i in range(len(x)):
    print(x[i])

#List compression
[print (i) for i in x]

#Using Enumerator
for index,element in enumerate(x):
    print(f'{index} {element}')