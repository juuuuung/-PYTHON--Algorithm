# Bubble sort

def swap(i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

arr = [1,5,7,3,8,9,2,6,10,4]

for i in range(len(arr)):
    for j in range(len(arr) - (i+1)):
        if arr[j] > arr[j+1]:
            swap(j, j+1)
            print(arr)
    
print(arr)
