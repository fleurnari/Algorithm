import sys
input = sys.stdin.readline
s = input().rstrip()
pos = {}

for i, c in enumerate(s):
  if c not in pos:
    pos[c] = [i]
  else:
    pos[c].append(i)

answer = 0
keys = list(pos.keys())

for i in range(len(keys)):
  a = keys[i]
  a1, a2 = pos[a]
  for j in range(i + 1, len(keys)):
    b = keys[j]
    b1, b2 = pos[b]
    if (a1 < b1 < a2 < b2) or (b1 < a1 < b2 < a2):
      answer += 1

print(answer)