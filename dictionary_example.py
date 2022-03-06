map = {}

map['a'] = 1
map['b'] = 2
print(map.keys())
print(map.values())
print(map.items())

map.pop('a')
print(map.items())
print(map.get('a'))
print(map.get('b'))
# print(map['a'])
