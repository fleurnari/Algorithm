import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
b = [list(input().rstrip()) for _ in range(n)]
cnt = 0

def flip(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = '1' if a[i][j] == '0' else '0'


for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            flip(i, j)
            cnt += 1

if a == b:
    print(cnt)
else:
    print(-1)