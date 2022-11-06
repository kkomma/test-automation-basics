print('hello')
a=[1,2,3,1]
for i in range(0,len(a),1):
	print(a[i])
for i in range(len(a),0,-1):
	print(a[-i])
print(a)
print(a[:2])
print(a[2:])
print(a[-2:])
print(a[::-1])
print(set(a))
for i in set(a):
	print(i,a.count(i))
print(ord('a')) 
print(4>>1)
print(4<<1)
print(5/2)
print(5//2)
s='abca'
print(sorted(set(s)))
for i in range(len(s)):
	print(s[i])
	
for i in s:
	print(i)