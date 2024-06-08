def kingPath(n,m):
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 or j==1:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]+dp[i-1][j-1]
    return dp[-1][-1]

if __name__ == '__main__':
    n = 3
    m = 3
    print(kingPath(n,m))

    n = 3
    m = 2
    print(kingPath(n,m))

    n = 8
    m = 8
    print(kingPath(n,m))

    n = 3
    m = 1
    print(kingPath(n,m))

    n = 1
    m = 3
    print(kingPath(n,m))