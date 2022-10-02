#Insert sort


def swap(i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

arr = [1,5,7,3,8,9,2,6,10,4]
for key in range(1, len(arr)):
    j = key
    while arr[j-1] > arr[j]:
        swap(j-1, j)
        j-=1

print(arr)