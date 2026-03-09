import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
ans = [0] * n

for i in range(n - 1):
    maxSlope = -sys.maxsize
    for j in range(i + 1, n):
        slope = (a[j] - a[i]) / (j - i)
        if slope > maxSlope:
            maxSlope = slope
            ans[i] += 1
            ans[j] += 1

print(max(ans))