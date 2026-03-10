import sys
input = sys.stdin.readline
n = input().rstrip()
cnt = [0] * 10

for i in n:
    cnt[int(i)] += 1

cnt[6] = (cnt[6] + cnt[9] + 1) // 2
cnt[9] = 0

print(max(cnt))