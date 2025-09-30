import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
answer = 0

def recur(x, y, n):
  global answer
  if x == r and y == c:
    print(answer)
    exit(0)
  if n == 1:
    answer += 1
    return
  if not (x <= r < x + n and y <= c < y + n):
    answer += n * n
    return
  tmp = n // 2
  recur(x, y, tmp)
  recur(x, y + tmp, tmp)
  recur(x + tmp, y, tmp)
  recur(x + tmp, y + tmp, tmp)

recur(0, 0, 2 ** n)
print(answer)