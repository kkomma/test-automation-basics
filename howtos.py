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
print(chr(97))
print('shifting')
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


i = str(4)
print(isinstance(i,str))

s='appleincorporated'
a=[]

for ss in s:
    a.append(ss)
print(a)    

print(s.count('e'))

from collections import Counter
counter = Counter("Mary had a little lamb")
print(counter['a'])

t='al223pha4345?nums!'

nums = []
lettrs = []
notalnums = []
for ss in t:
    if ss.isdigit():
        nums.append(ss)

for ss in t:
    if ss.isalpha():
        lettrs.append(ss)

for ss in t:
    if not ss.isalnum():
        notalnums.append(ss)

print(nums)        
print(lettrs)        
print(notalnums)        	

if __name__ == '__main__':
    pass
            