import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
s = input().rstrip()
n = len(s)
palindrome = [[0 for _ in range(n)] for _ in range(n)]
dpTable = [2500] * (n + 1)
dpTable[-1] = 0

for i in range(n):
  palindrome[i][i] = 1

for i in range(n - 1, -1, -1):
  for j in range(i + 1, n):
    if s[i] == s[j]:
      if j - i == 1:
        palindrome[i][j] = 1
      else:
        palindrome[i][j] = palindrome[i + 1][j - 1]

for end in range(n):
  for start in range(end + 1):
    if palindrome[start][end]:
      dpTable[end] = min(dpTable[end], dpTable[start - 1] + 1)

print(dpTable[n - 1])