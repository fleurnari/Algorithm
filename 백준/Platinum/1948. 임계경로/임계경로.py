import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
cityList = [[] for i in range(n + 1)]
reverseCity = [[] for i in range(n + 1)]
cityChk = [0] * (n + 1)
visited = [False] * (n + 1)
result = [0] * (n + 1)
resultCnt = 0


for i in range(m):
  s, e, v = map(int, input().split())
  cityList[s].append((e, v))
  reverseCity[e].append((s, v))
  cityChk[e] += 1

startCity, endCity = map(int, input().split())

queue = deque()
queue.append(startCity)

while queue:
  now = queue.popleft()
  for i in cityList[now]:
    cityChk[i[0]] -= 1
    result[i[0]] = max(result[i[0]], result[now] + i[1])
    if cityChk[i[0]] == 0:
      queue.append(i[0])

queue.clear()
queue.append(endCity)
visited[endCity] = True

while queue:
  now = queue.popleft()
  for i in reverseCity[now]:
    if result[i[0]] + i[1] == result[now]:
      resultCnt += 1
      if not visited[i[0]]:
        visited[i[0]] = True
        queue.append(i[0])
        
print(result[endCity])
print(resultCnt)