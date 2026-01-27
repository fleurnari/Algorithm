import sys
input = sys.stdin.readline
n = int(input())

def dfs(path):
  if len(path) == length:
    print(''.join(path))
    return

  for ch in chars:
    if counter[ch] > 0:
      counter[ch] -= 1
      path.append(ch)
      dfs(path)
      path.pop()
      counter[ch] += 1

for _ in range(n):
  word = input().strip()
  word = sorted(word)
  length = len(word)
  counter = {}
  for c in word:
    counter[c] = counter.get(c, 0) + 1
  chars = sorted(counter.keys())
  dfs([])