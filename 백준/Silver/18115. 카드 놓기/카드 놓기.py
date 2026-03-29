import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.reverse()
dq = deque()

for i in range(n):
    if a[i] == 1:
        dq.appendleft(i + 1)
    elif a[i] == 2:
        dq.insert(1, i + 1)
    elif a[i] == 3:
        dq.append(i + 1)

print(*dq)