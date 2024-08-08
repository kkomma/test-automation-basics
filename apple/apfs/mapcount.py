
from collections import defaultdict
from collections import OrderedDict

m = defaultdict(int)
o = OrderedDict()
s='teslainchighlyvalued'
for i in s:
    m[i] += 1
    o[i] = m[i]

print(m)
for k,v in m.items():
    print(k,v) 

print('ordered dict')
print(o)
print(o.keys()) 
print(o.move_to_end('t'))  
print(o.keys()) 
o.popitem(last=False)
print(o.keys()) 
o.popitem()
print(o.keys()) 