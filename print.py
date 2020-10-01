n = int(input())
k = 0
m = 0

for i in range(1, n+1):
    k = (2*i)-1
    m = i
    for j in range(1, k+1):
        print(m, end="")
        if j < i:
            m += 1
        else:
            m -= 1
    print()

for i in range(n-1, 0,-1):
    k = (2*i)-1
    m = i
    for j in range(1, k+1):
        print(m, end="")
        if j < i:
            m += 1
        else:
            m -= 1
    print()