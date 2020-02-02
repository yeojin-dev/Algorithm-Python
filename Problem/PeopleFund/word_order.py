from collections import defaultdict

num = int(input())

word_set = set()
word_list = list()
word_count = defaultdict(int)

word_set_length = len(word_set)

for i in range(num):
    word = input()
    word_set.add(word)
    new_word_set_length = len(word_set)
    if word_set_length != new_word_set_length:
        word_list.append(word)
        word_set_length += 1
    word_count[word] += 1

result = ' '.join(str(word_count[word]) for word in word_list)

print(word_set_length)
print(result)
