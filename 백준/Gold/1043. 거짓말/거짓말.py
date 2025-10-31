import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trueKnow = list(map(int, input().split()))
true = trueKnow[0]
del trueKnow[0]
answer = 0
party = [[] for _ in range(m)]
parent = [0] * (n + 1)

def find(a):
  if parent[a] == a:
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a

for i in range(n + 1):
  parent[i] = i

for i in range(m):
  party[i] = list(map(int, input().split()))
  del party[i][0]

for i in range(m):
  first = party[i][0]
  for j in range(1, len(party[i])):
    union(first, party[i][j])

for i in range(m):
  isPossible = True
  first = party[i][0]
  for j in range(len(trueKnow)):
    if find(first) == find(trueKnow[j]):
      isPossible = False
      break
  if isPossible:
    answer += 1

print(answer)