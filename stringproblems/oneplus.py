a = [1,2,3]
# a = [9,8,7,6,5,4,3,2,1,0]
# a = [9,9,9,9,9,9,9,9,9,9]
s = "".join(str(x) for x in a)
print(s)
i = int(s) +1
print([int(digit) for digit in str(i)])