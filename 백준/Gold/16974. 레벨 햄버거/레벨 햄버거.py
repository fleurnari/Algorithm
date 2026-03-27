import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, x = map(int, input().split())
length = [0] * (n + 1)
patty = [0] * (n + 1)
length[0] = 1
patty[0] = 1

for i in range(1, n + 1):
    length[i] = length[i - 1] * 2 + 3
    patty[i] = patty[i - 1] * 2 + 1

def solve(n, x):
    if n == 0:
        return 1 if x >= 1 else 0

    if x == 1:
        return 0
    elif x <= 1 + length[n - 1]:
        return solve(n - 1, x - 1)
    elif x == 1 + length[n - 1] + 1:
        return patty[n - 1] + 1
    elif x <= 1 + length[n - 1] + 1 + length[n - 1]:
        return patty[n - 1] + 1 + solve(n - 1, x - (length[n - 1] + 2))

    else:
        return patty[n]

print(solve(n, x))