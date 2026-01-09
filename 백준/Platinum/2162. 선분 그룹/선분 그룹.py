import sys
input = sys.stdin.readline
n = int(input())
parent = [-1] * (3001)
line = []
line.append([])
group = 0
cnt = 0

def ccw(x1, y1, x2, y2, x3, y3):
  tmp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
  if tmp > 0:
    return 1
  elif tmp < 0:
    return -1
  else:
    return 0

def overlab(x1, y1, x2, y2, x3, y3, x4, y4):
  if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
    return True
  return False

def cross(x1, y1, x2, y2, x3, y3, x4, y4):
  abc = ccw(x1, y1, x2, y2, x3, y3)
  abd = ccw(x1, y1, x2, y2, x4, y4)
  cda = ccw(x3, y3, x4, y4, x1, y1)
  cdb = ccw(x3, y3, x4, y4, x2, y2)
  if abc * abd == 0 and cda * cdb == 0:
    return overlab(x1, y1, x2, y2, x3, y3, x4, y4)
  elif abc * abd <= 0 and cda * cdb <= 0:
    return True
  return False

def find(a):
  if parent[a] < 0:
    return a
  parent[a] = find(parent[a])
  return parent[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a == b:
    return
  parent[a] += parent[b]
  parent[b] = a

for i in range(1, n + 1):
  line.append([])
  line[i] = list(map(int, input().split()))
  for j in range(1, i):
    if cross(line[i][0], line[i][1], line[i][2], line[i][3], line[j][0], line[j][1], line[j][2], line[j][3]):
      union(i, j)

for i in range(1, n + 1):
  if parent[i] < 0:
    group += 1
    cnt = min(cnt, parent[i])

print(group)
print(-cnt)