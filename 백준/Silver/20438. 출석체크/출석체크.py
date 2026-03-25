import sys
input = sys.stdin.readline
n, k, q, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sleep = [False] * (n + 3)
checked = [False] * (n + 3)

for x in a:
    sleep[x] = True

for x in b:
    if sleep[x]:
        continue
    for i in range(x, n + 3, x):
        if not sleep[i]:
            checked[i] = True

prefix = [0] * (n + 3)

for i in range(3, n + 3):
    if not checked[i]:
        prefix[i] = prefix[i - 1] + 1
    else:
        prefix[i] = prefix[i - 1]

for _ in range(m):
    s, e = map(int, input().split())
    print(prefix[e] - prefix[s - 1])