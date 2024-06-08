class StaticClass:
    def workWithArray(self,s,beginIdx,endIdx):
        self.reverse_words(s,beginIdx,endIdx)

    def reverse_words(self,s,beginIdx,endIdx):
        s[beginIdx:endIdx] = s[beginIdx:endIdx][::-1]
        # while beginIdx < endIdx:
        #     s[beginIdx], s[endIdx] = s[endIdx], s[beginIdx] #TypeError: 'str' object does not support item assignment
        #     beginIdx += 1
        #     endIdx -=1
    
# a=[1, 2, 3, 4, 5,6,7,8]
a = 'this is a test'
a = list(a)
obj = StaticClass()
obj.workWithArray(a,3,6)    
print(a)