num = input()
curr_n = 0
next_n = 0
first_n = num[0]
last_n = num[-1]
tot_sum = 0

for i in range(0, len(num)-1):

    if num[i] == num[i+1]:
        curr_n = i+1
        if int(num[i])%2==0:
            tot_sum += int(num[i])*curr_n
        else:
            tot_sum += int(num[i])

if last_n == first_n:
    if int(num[i])%2==0:
        tot_sum += int(last_n)*len(num)
    else:
        tot_sum += int(last_n)
        

print(tot_sum)