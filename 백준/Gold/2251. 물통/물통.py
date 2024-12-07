from collections import deque

send = [0, 0, 1, 1, 2, 2]
receive = [1, 2, 0, 2, 0, 1]
before = list(map(int, input().split()))
visit = [[False for i in range(201)] for j in range(201)]
answer = [False] * 201

def BFS():
  queue = deque()
  queue.append((0, 0))
  visit[0][0] = True
  answer[before[2]] = True

  while queue:
    now = queue.popleft()
    a = now[0]
    b = now[1]
    c = before[2] - a - b

    for i in range(6):
      after = [a, b, c]
      after[receive[i]] += after[send[i]]
      after[send[i]] = 0

      if after[receive[i]] > before[receive[i]]:
        after[send[i]] = after[receive[i]] - before[receive[i]]
        after[receive[i]] = before[receive[i]]

      if not visit[after[0]][after[1]]:
        visit[after[0]][after[1]] = True
        queue.append((after[0], after[1]))

        if after[0] == 0:
          answer[after[2]] = True

BFS()

for i in range(len(answer)):
  if answer[i]:
    print(i, end = ' ')