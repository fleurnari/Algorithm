n, m = map(int, input().split())
trueList = list(map(int, input().split()))
trueCnt = trueList[0]
del trueList[0]
rep = [0] * (n + 1)
party = [[] for i in range(m)]
result = 0

for i in range(n + 1):
  rep[i] = i

for i in range(m):
  party[i] = list(map(int, input().split()))
  del party[i][0]

def find(a):
  if a == rep[a]:
    return a
  else:
    rep[a] = find(rep[a])
    return rep[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    rep[b] = a

def chkSame(a, b):
  a = find(a)
  b = find(b)
  if a == b:
    return True
  else:
    return False

for i in range(m):
  repPeople = party[i][0]
  for j in range(1, len(party[i])):
    union(repPeople, party[i][j])

for i in range(m):
  bLie = True
  repPeople = party[i][0]
  for j in range(len(trueList)):
    if find(repPeople) == find(trueList[j]):
      bLie = False
      break
  if bLie:
    result += 1

print(result)