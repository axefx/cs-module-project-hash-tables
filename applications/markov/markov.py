import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words_list = words.split()
word_pairs = []
for i in range(len(words_list) - 1):
    word_pairs.append((words_list[i],words_list[i + 1]))
word_map = {}
for w1,w2 in word_pairs:
    if w1 in word_map:
        word_map[w1].append(w2)
    else:
        word_map[w1] = [w2]


# TODO: construct 5 random sentences
# Your code here

