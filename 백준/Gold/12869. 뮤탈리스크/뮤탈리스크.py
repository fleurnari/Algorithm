import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
scv = list(map(int, input().split()))
visit = [[[False] * 61 for _ in range(61)] for _ in range(61)]
damage = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]
queue = deque()

while len(scv) < 3:
    scv.append(0)

queue.append((scv[0], scv[1], scv[2], 0))
visit[scv[0]][scv[1]][scv[2]] = True

while queue:
    a, b, c, cnt = queue.popleft()

    if a == 0 and b == 0 and c == 0:
        print(cnt)
        break

    for d1, d2, d3 in damage:
        na = max(0, a - d1)
        nb = max(0, b - d2)
        nc = max(0, c - d3)

        if not visit[na][nb][nc]:
            visit[na][nb][nc] = True
            queue.append((na, nb, nc, cnt + 1))