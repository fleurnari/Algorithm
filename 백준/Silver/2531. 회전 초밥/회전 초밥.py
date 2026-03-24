import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
sushi += sushi[:k - 1]
count = [0] * (d + 1)
cnt = 0

for i in range(k):
    if count[sushi[i]] == 0:
        cnt += 1
    count[sushi[i]] += 1

answer = cnt + (1 if count[c] == 0 else 0)

for i in range(1, n):
    l = sushi[i - 1]
    count[l] -= 1
    if count[l] == 0:
        cnt -= 1

    r = sushi[i + k - 1]
    if count[r] == 0:
        cnt += 1
    count[r] += 1

    tmp = cnt + (1 if count[c] == 0 else 0)
    answer = max(answer, tmp)

print(answer)