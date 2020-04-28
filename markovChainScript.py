import numpy as np

sample = open('words').read()

corpus = sample.split()

def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        yield (corpus[i], corpus[i + 1])

pairs = make_pairs(corpus)

self_mem = {}

for word_1, word_2 in pairs:
    if word_1 in self_mem.keys():
        self_mem[word_1].append(word_2)
    else:
        self_mem[word_1] = [word_2]
first_word = np.random.choice(corpus)

if first_word.islower():
    first_word = np.random.choice(corpus)

chain = [first_word]

num_words = 150

for i in range(num_words):
    chain.append(np.random.choice(self_mem[chain[-1]]))

print(' '.join(chain))
