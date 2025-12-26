import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visitList = [[0] * m for _ in range(n)]
groupNum = 1
dic = dict()

for _ in range(n):
  graph.append(list(map(int, input().strip())))

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0 and not visitList[i][j]:
      tmpCnt = 1
      queue = deque()
      queue.append((i, j))
      visitList[i][j] = groupNum
      while queue:
        x, y = queue.popleft()
        for k in range(4):
          nx = x + dx[k]
          ny = y + dy[k]
          if 0 <= nx < n and 0 <= ny < m and not visitList[nx][ny] and graph[nx][ny] == 0:
              queue.append((nx, ny))
              visitList[nx][ny] = groupNum
              tmpCnt += 1
      dic[groupNum] = tmpCnt
      groupNum += 1

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      print(0, end = '')
    else:
      answer = 0
      setList = set()
      for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < m and visitList[nx][ny] != 0:
          setList.add(visitList[nx][ny])
      setList = list(setList)
      for k in setList:
        answer += dic[k]
      print((answer + 1) % 10, end = '')
  print()