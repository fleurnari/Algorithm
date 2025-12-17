import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  n = int(input())
  s = [0] + list(map(int, input().split()))
  visitList = [False] * (n + 1)
  teamMember = 0

  def dfs(i):
    global teamMember
    visitList[i] = True
    team.append(i)
    next = s[i]

    if not visitList[next]:
      dfs(next)
    else:
      if next in team:
        teamMember += len(team[team.index(next):])

  for i in range(1, n + 1):
    if not visitList[i]:
      team = []
      dfs(i)

  print(n - teamMember)