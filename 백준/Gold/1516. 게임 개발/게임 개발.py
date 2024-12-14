from collections import deque
n = int(input())
bdList = [[] for i in range(n + 1)]
bdChk = [0] * (n + 1)
buildTime = [0] * (n + 1)
result = [0] * (n + 1)

for i in range(1, n + 1):
  inputList = list(map(int, input().split()))
  buildTime[i] = inputList[0]
  idx = 1
  while True:
    tmp = inputList[idx]
    idx += 1
    if tmp == -1:
      break
    bdList[tmp].append(i)
    bdChk[i] += 1

queue = deque()

for i in range(1, n + 1):
  if (bdChk[i] == 0):
    queue.append(i)

while queue:
  now = queue.popleft()
  for i in bdList[now]:
    bdChk[i] -= 1
    result[i] = max(result[i], result[now] + buildTime[now])
    if bdChk[i] == 0:
      queue.append(i)

for i in range(1, n + 1):
  print(result[i] + buildTime[i])