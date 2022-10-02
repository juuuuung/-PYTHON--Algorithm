# Select sort


def swap(i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

arr = [1,5,7,3,8,9,2,6,10,4]

for i in range(len(arr)-1):
    index = 0
    min = max(arr);
    for j in range(i, len(arr)):
        if min > arr[j]:
            min = arr[j]
            index = j
    swap(i, index)

print(arr)
