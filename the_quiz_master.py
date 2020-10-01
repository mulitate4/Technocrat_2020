import math

p_q = input()
p, q = p_q.split(" ")

p = int(p)
q = int(q)

answers = []
for i in range(0, p):
    answers.append(input())
answer_str = input()

counter = 0
res_arr = []

for x, i in enumerate(answers):
    counter = 0
    for y, j in enumerate(i):
        if j == answer_str[y]:
            counter += 1
     
    res_arr.append(counter)
    print(f"Participant{x+1} = {counter}")

ind = 0
maxs = 0
for i in range(0, len(res_arr)):
    if maxs < res_arr[i]:
        maxs=res_arr[i]
        ind = i

print(f"Winner is Participant{ind+1} = {maxs}")