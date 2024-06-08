from collections import deque
from collections import deque, Counter, defaultdict, OrderedDict

# a = [3,1,2,4]
# # op=[2,4,3,1]
# l=[]
# m=[]
# for aa in a:
#     if aa%2==0:
#         l.append(aa)
#     else:
#         m.append(aa)
# l.extend(m)
# print(l)
      
a = [3, 1, 2, 4]
# op=[2, 4, 3, 1]

d = deque()

for aa in a:
    if aa % 2 == 0:
        d.appendleft(aa)
    else:
        d.append(aa)

print(list(d))

# Example code for using all functions in the collections module


# deque example
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)  # Output: deque([0, 1, 2, 3, 4])

# Counter example
c = Counter([1, 2, 2, 3, 3, 3])
print(c)  # Output: Counter({3: 3, 2: 2, 1: 1})

# defaultdict example
d = defaultdict(int)
d['a'] += 1
d['b'] += 2
print(d)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d['a'])

# OrderedDict example
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])