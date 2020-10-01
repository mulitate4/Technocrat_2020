sentence = input()
words = sentence.split(" ")

words_arr = []

def sort_l(word:list):
    return sorted(word, reverse=True)

def split_word(word):
    return [lett for lett in word]

def all_except(word: list):
    first_lett = ord(word[0])
    last_lett = ord(word[-1])
    all_except_str = ""

    for i in range(int(last_lett+1), int(first_lett)):
        x = chr(i)
        if x in word:
            continue
        else:
            all_except_str += chr(i)

    all_except_str += " "
    return all_except_str

sorted_str = ""
all_except_cmp_str = ""

for i in words:
    x = sort_l(split_word(i))
    all_except_cmp_str += all_except(x)
    for lett in x:
        sorted_str += lett
    sorted_str += " "
    
print(sorted_str)
print(all_except_cmp_str)