arr = input()
p, q = arr.split(" ")
arr_1 = []
arr_2 = []

for i in range(0, int(p)):
    arr_1.append(input())

for i in range(0, int(q)):
    arr_2.append(input())

arr_1u2 = []

arr1_len = len(arr_1)
arr2_len = len(arr_2)

lesser = 1

if arr1_len > arr2_len:
    lesser = arr2_len
else:
    lesser = arr1_len

k=0
for i in range(0, lesser*2):
    if i%2==0:
        arr_1u2.append(arr_1[k])
        continue
    else:
        arr_1u2.append(arr_2[k])
    k+=1

for i in range(lesser*2, arr1_len + arr2_len):
    if lesser == arr2_len:
        arr_1u2.append(arr_1[k])
    else:
        arr_1u2.append(arr_2[k])
    k+=1

for num in arr_1u2:
    print(num, end=" ")