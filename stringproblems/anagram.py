from collections import Counter


class Anagram:

    def checkAnagrammap(s,t):       
        a = Counter(s)
        b = Counter(t)
        print('a',a)
        print('b',b)
        if a == b:
            return True
        else:
            return False        
    
    def checkAnagram(s,t):
        a = [0]*26
        b = [0]*26
        for c in s:
            a[ord(c)-ord('a')]+=1
        for c in t:
            b[ord(c)-ord('a')]+=1            
        if a == b:
            return True
        else:
            return False

if __name__== '__main__':
    print(Anagram.checkAnagrammap('anagram','nagaram')) # True
    print(Anagram.checkAnagram('anagram','nagaram')) # True
    print(Anagram.checkAnagram('rat','car')) # False
    print(Anagram.checkAnagram('a','a')) # True
    print(Anagram.checkAnagram('ab','a')) # False
    print(Anagram.checkAnagram('a','ab')) # False
    print(Anagram.checkAnagram('a','b')) # False
    print(Anagram.checkAnagram('a','')) # False
    print(Anagram.checkAnagram('','a')) # False
    print(Anagram.checkAnagram('','')) # True
    print('counters')
    print(Anagram.checkAnagrammap('','')) # True
    print(Anagram.checkAnagram('a','')) # False
    print(Anagram.checkAnagram('','a')) # False
                                       