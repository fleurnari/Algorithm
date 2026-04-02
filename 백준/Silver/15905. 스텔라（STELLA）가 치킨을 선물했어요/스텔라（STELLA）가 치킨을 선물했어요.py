import sys
input = sys.stdin.readline
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : (-x[0], x[1]))
fifth = arr[4]
cnt = 0

for i in range(5, n):
    if arr[i][0] == fifth[0]:
        cnt += 1

print(cnt)