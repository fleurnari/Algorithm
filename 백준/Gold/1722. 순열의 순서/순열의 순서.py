import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
fac = [0] * 21
fac[0] = 1
seq = [0] * 21
visit = [False] * 21

for i in range(1, n + 1):
    fac[i] = fac[i - 1] * i

if data[0] == 1:
    k = data[1]
    for i in range(1, n + 1):
        cnt = 1
        for j in range(1, n + 1):
            if visit[j]:
                continue
            if k <= cnt * fac[n - i]:
                k -= (cnt - 1) * fac[n - i]
                seq[i] = j
                visit[j] = True
                break
            cnt += 1
    for i in range(1, n + 1):
        print(seq[i], end = ' ')
else:
    k = 1
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, data[i]):
            if not visit[j]:
                cnt += 1
        k += cnt * fac[n - i]
        visit[data[i]] = True
    print(k)