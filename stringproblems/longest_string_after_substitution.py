
def characterreplacement(s,k):
    curLen = 0
    l = 0
    r = 0
    maxVar = 0
    arrVals = [0] * 26  # Assuming only uppercase English characters
    
    while r < len(s):
        arrVals[ord(s[r]) - ord('A')] += 1
        maxVar = max(maxVar, arrVals[ord(s[r]) - ord('A')])
        
        if r - l + 1 - maxVar > k:
            arrVals[ord(s[l]) - ord('A')] -= 1
            l += 1
        
        curLen = max(curLen, r - l + 1)
        r += 1
    
    return curLen

    
if __name__ == '__main__':
    s = "ABBB" 
    k = 2
    print(characterreplacement(s,k))

    s = "AAABABB" 
    k = 1
    print(characterreplacement(s,k))

    s = "XYYX" 
    k = 2
    print(characterreplacement(s,k))

    s = "AAAB" 
    k = 0
    print(characterreplacement(s,k))

  