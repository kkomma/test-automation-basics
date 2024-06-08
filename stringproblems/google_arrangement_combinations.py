import math
import itertools

s = 'abc'
n = len(s)
r = 2

# Generate all arrangements
a = math.perm(n, r)
b = [''.join(a) for a in itertools.permutations(s, r)]

# Generate all combinations
c = math.comb(n, r)
d = list(itertools.combinations(s, r))

print(a)
print(b)
print(c)
print(d)