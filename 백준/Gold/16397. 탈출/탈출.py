import sys
from collections import deque
input = sys.stdin.readline
n, t, g = map(int, input().split())
visit = [False] * 100000
queue = deque()
queue.append((n, 0))
visit[n] = True

while queue:
    x, cnt = queue.popleft()

    if cnt > t:
        continue
    if x == g:
        print(cnt)
        exit()

    nx = x + 1
    if nx < 100000 and not visit[nx]:
        visit[nx] = True
        queue.append((nx, cnt + 1))

    if x != 0:
        nx = x * 2
        if nx < 100000:
            nx = int(str(nx))
            s = str(nx)
            nx -= 10 ** (len(s) - 1)
            if not visit[nx]:
                visit[nx] = True
                queue.append((nx, cnt + 1))

print("ANG")