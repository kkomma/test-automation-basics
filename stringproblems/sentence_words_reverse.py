

def reverse_words_in_sentence(s):
    words = s.split(' ')
    print('lenn',len(words))
    print('----')
    for word in words:        
        print(word)
    print('----')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

input_string = ' we dev    loop '
reversed_string = reverse_words_in_sentence(input_string)
print(reversed_string)

class ReverseString:
    def reverse_words(self,s):
        s = list(s)
        print('s::',s)
        flag = True
        beginIdx = 0
        for index in range(len(s)-1):
            if s[index].isalpha():
                if flag:
                    beginIdx = index-1
                    print('beginIdx::',beginIdx)
                    flag = False
                print('char::',s[index])
            else:
                endIdx = index
                print('endIdx::',endIdx)
                if beginIdx > 0:
                    while beginIdx < endIdx:
                        s[beginIdx], s[endIdx] = s[endIdx], s[beginIdx]
                        beginIdx += 1
                        endIdx -=1
                    beginIdx=0
                    endIdx=0
                    flag = True
        return s

obj = ReverseString()
input_string = ' we dev    loop  '
print(obj.reverse_words(input_string))

input_string = '  we dev    loop   '
cc =input_string.count(' ')
print(cc)

from collections import Counter
cc =Counter(input_string)
print(cc)

input_string = '  we dev    loop   '
cc =input_string.split(' ')
print(len(cc))
print('===============')
for c in cc:
    if c.isalpha():
        print(c)
    elif c == '':
        print('emptyspace')
    else:
        print('space::',ascii(c))