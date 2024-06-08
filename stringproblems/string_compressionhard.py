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