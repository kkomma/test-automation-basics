def permute(s):
    def dfs(path, used, result):
        if len(path) == len(s):
            result.append(path)
            return
        for i in range(len(s)):
            if not used[i]:
                used[i] = True
                dfs(path + s[i], used, result)
                used[i] = False
    result = []
    used = [False] * len(s)
    dfs("", used, result)
    return result

print(permute("abc"))


def combine(s, k):
    def dfs(path, index, k, result):
        if len(path) == k:
            result.append(path)
            return
        for i in range(index, len(s)):
            dfs(path + s[i], i + 1, k, result)
    result = []
    dfs("", 0, k, result)
    return result

print(combine("abc", 2))