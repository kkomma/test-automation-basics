import math
import itertools

s = 'abc'
n = len(s)
r = 2

# A permutation is an act of arranging objects or numbers in order. 
# Combinations are the way of selecting objects or numbers from a group of objects or collections, 
# in such a way that the order of the objects does not matter.
# An example of permutations is the number of 2 letter words that can be formed by using the letters in a word say, GREAT; 5P_2 = 5!/(5-2)! 
# An example of combinations is in how many combinations we can write the words using the vowels of the word GREAT; 5C_2 =5!/[2! (5-2)!]
# The formula for permutations is: nPr = n!/(n-r)! The formula for combinations is: nCr = n!/[r! (n-r)!]


# Generate all arrangements
ss = itertools.permutations(s, r)
for s in ss:
    print('pp::',*s)
a = math.perm(n, r)
print('a:', a)
b = [''.join(a) for a in itertools.permutations(s, r)]
print('b', b)

# Generate all combinations
ss = itertools.combinations(s, r)
for s in ss:
    print('cc::',*s)
c = math.comb(n, r)
print('c', c)
d = list(itertools.combinations(s, r))
print('d', d)
