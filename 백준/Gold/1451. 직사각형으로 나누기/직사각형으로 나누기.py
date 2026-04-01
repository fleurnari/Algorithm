import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
prefix = [[0] * (m + 1) for _ in range(n + 1)]
answer = 0

for i in range(n):
    for j in range(m):
        prefix[i + 1][j + 1] = (arr[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j])

def getSum(x1, y1,x2, y2):
    return (prefix[x2][y2] - prefix[x1][y2] - prefix[x2][y1] + prefix[x1][y1])

for i in range(1, m - 1):
    for j in range(i + 1, m):
        a = getSum(0, 0, n, i)
        b = getSum(0, i, n, j)
        c = getSum(0, j, n, m)
        answer = max(answer, a * b * c)

for i in range(1, n - 1):
    for j in range(i + 1, n):
         a = getSum(0, 0, i, m)
         b = getSum(i, 0, j, m)
         c = getSum(j, 0, n, m)
         answer = max(answer, a * b * c)

for i in range(1, m):
    for j in range(1, n):
         a = getSum(0, 0, n, i)
         b = getSum(0, i, j, m)
         c = getSum(j, i, n, m)
         answer = max(answer, a * b * c)


for i in range(1, m):
     for j in range(1, n):
          a = getSum(0, 0, j, i)
          b = getSum(j, 0, n, i)
          c = getSum(0, i, n, m)
          answer = max(answer, a * b * c)


for i in range(1, n):
     for j in range(1, m):
         a = getSum(0, 0, i, m)
         b = getSum(i, 0, n, j)
         c = getSum(i, j, n, m)
         answer = max(answer, a * b * c)

for i in range(1, n):
    for j in range(1, m):
        a = getSum(0, 0, i, j)
        b = getSum(0, j, i, m)
        c = getSum(i, 0, n, m)
        answer = max(answer, a * b * c)

print(answer)