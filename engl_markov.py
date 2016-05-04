import string

from numpy import cumsum, sort, sum, searchsorted
from numpy.random import rand

# params

num_chars = 140

# helper functions

def char_to_index(c):
    if c == ' ':
        return 0
    else:
        return ord(c) - 96

def index_to_char(i):
    if i == 0:
        return ' '
    else:
        return chr(i + 96)

def weighted_pick(weights):
    t = cumsum(weights)
    s = sum(weights)
    a = searchsorted(t, rand(1) * s)
    return a[0]

# load the text

alice = ''

with open('alice.txt', 'r') as f:
    for line in f:
        alice += line

alice = alice.translate(string.maketrans("",""), string.punctuation).lower().replace('\n', ' ').replace('  ', ' ')

# build the chain

P = [[0 for x in range(27)] for x in range(27)]

for i in range(1, len(alice)):
    r = char_to_index(alice[i-1])
    c = char_to_index(alice[i])
    P[r][c] += 1

for r in range(27):
    total = 0.0
    for c in range(27):
        total += P[r][c]
    P[r] = [x / total for x in P[r]]

# make some gibberish

out = ' '
for i in range(num_chars):
    j = char_to_index(out[i])
    out += index_to_char(weighted_pick(P[j]))

out = out[1:]

# print said gibberish

print(out)
