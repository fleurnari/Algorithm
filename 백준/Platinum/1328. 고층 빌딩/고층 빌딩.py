import sys
input = sys.stdin.readline
n, l, r = map(int, input().split())
mod = 1000000007
dpTable = [[[0 for k in range(101)] for j in range(101)] for i in range(101)]
dpTable[1][1][1] = 1

for i in range(2, n + 1):
    for j in range(1, l + 1):
        for k in range(1, r + 1):
            dpTable[i][j][k] = (dpTable[i - 1][j - 1][k] + dpTable[i - 1][j][k - 1] + dpTable[i - 1][j][k] * (i - 2)) % mod
            
print(dpTable[n][l][r])