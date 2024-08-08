def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # print(dp)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print('dp', dp[i][j])
    return dp[m][n]

def longestSubsequence(x, y):
    subStrings = []
    for i in range(len(x)):
        for j in range(i+1, len(x)+1):
            subStrings.append(x[i:j])
    maxLength = 0
    
    for subString in subStrings:
        temp = ''
        y_temp = y
        for char in subString:
            if char in y_temp:
                temp += char
                y_temp = y_temp.replace(char, '', 1)                
        maxLength = max(maxLength, len(temp))
    return maxLength

X = "hackerranks"
Y = "hackers"
# X="abc"
# Y="aedace"

# print(lcs(X, Y))
print(longestSubsequence(X, Y))