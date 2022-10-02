import sys

# def swap(i, j):
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp

n = int(input())

arr = [int(sys.stdin.readline()) for _ in range (n)]

for a in sorted(arr):
    print(a)

# for i in range(len(arr)):
#     index = i
#     for j in range(i, len(arr)):
#         if arr[index] > arr[j]:
#             swap(index, j)

# for a in arr:
#     print(a)