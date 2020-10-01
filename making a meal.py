n = int(input())
strings_list = []
code_chef_dict = {
    'c':0,
    'o':0,
    'd':0,
    'e':0,
    'h':0,
    'f':0,
}

code_chef_cnt = 0

for i in range(0, n):
    strings_list.append(input())

letters_list = []

for string in strings_list:
    for letter in string:
        letters_list.append(letter)

#codechef
for x, letter in enumerate(letters_list):
    if letter in code_chef_dict.keys():
        code_chef_dict[letter] += 1
    
while code_chef_dict['c'] >= 2 and code_chef_dict['o'] >= 1 and code_chef_dict['d'] >= 1 and code_chef_dict['e'] >= 2 and code_chef_dict['h'] >= 1 and code_chef_dict['f'] >= 1:
    code_chef_cnt += 1
    code_chef_dict['c'] -= 2
    code_chef_dict['o'] -= 1
    code_chef_dict['d'] -= 1
    code_chef_dict['e'] -= 2
    code_chef_dict['h'] -= 1
    code_chef_dict['f'] -= 1

print(code_chef_cnt)