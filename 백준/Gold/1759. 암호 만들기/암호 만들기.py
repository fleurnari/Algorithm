import sys
input = sys.stdin.readline
l, c = map(int, input().split())
arr = sorted(list(input().split()))
vowels = ['a', 'e', 'i', 'o', 'u']

def dfs(start, vowel, consonant, password):
    if len(password) == l:
        if vowel >= 1 and consonant >= 2:
            print(password)
        return
    for i in range(start, c):
        if arr[i] in vowels:
           dfs(i + 1, vowel + 1, consonant, password + arr[i])
        else:
           dfs(i + 1, vowel, consonant + 1, password + arr[i])

dfs(0, 0, 0, "")