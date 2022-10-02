arr = [3,5,1,6,9,7,4,2,10,8,12,41,512,3,51,2125,124]
# arr = [1,2,3,4,5,6,7,8,9,10]

def swap(i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

#Quik sort ver- 재귀
# def quik(start, end):
#     # 원소 값이 하나 일때 ex) 1 2 | 3 | 4 6 8 ~ 10
#     if start >= end:
#         return
    
#     key = start
#     i = key + 1
#     j = end

#     while i < j:
        
#         while arr[i] < arr[key]:
#             i += 1

#         # 왜 여기에 and j > key를 해줘야 할까? 그이유는 start부분 까지 가서 -1을 하면 더이상 index가 업기 때문 
#         while arr[j] > arr[key]: 
#             j -= 1
        
#         if i >= j:
#             swap(key, j)
#         else:
#             swap(i, j)

#     quik(start, j-1) # 왼쪽 집합 부분
#     quik(j+1, end) #오른쪽 집합 부분

# quik(0, len(arr)-1)
# print(arr)

def quik(start, end):
    if start >= end:
        return
    
    key = start
    i = start +1
    j = end

    while i < j:
        while arr[i] < arr[key]:
            i += 1
        
        while arr[j] > arr[key] and j > start:
            j -= 1
        
        if i > j:
            swap(key, j)
        else :
            swap(i, j)
        

    quik(start, j-1)
    quik(j+1, end)

quik(0, len(arr)-1)

print(arr)
        