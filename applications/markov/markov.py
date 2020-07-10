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
def get_start_words(words_list):
    return [word for word in words_list if word[0].isupper() or (word[0] == '"' and word[1].isupper())]

def is_stop_word(word):
    ends = ['.', '?', '!']
    return word[-1] in ends or (word[-1] == '"' and word[-2] in ends)

def get_next_words(word,word_map):
    return word_map[word]


def create_sentence(word_map):
    rand_start_word = random.choice(get_start_words(words_list))
    next_word = random.choice(get_next_words(rand_start_word,word_map))
    sentence = [rand_start_word]
    while not is_stop_word(next_word):
        sentence.append(next_word)
        next_word = random.choice(get_next_words(next_word,word_map))
    sentence.append(next_word)
    return ' '.join(sentence)

for i in range(5):
    sentence = create_sentence(word_map)
    print(sentence)