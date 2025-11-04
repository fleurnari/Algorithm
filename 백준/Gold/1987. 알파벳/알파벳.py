import sys
input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 1
visitList = [0] * 128
visitList[ord(arr[0][0])] = 1

def dfs(x, y, cnt):
  global answer
  answer = max(answer, cnt)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < r and 0 <= ny < c:
      if visitList[ord(arr[nx][ny])] == 0:
        visitList[ord(arr[nx][ny])] = 1
        dfs(nx, ny, cnt + 1)
        visitList[ord(arr[nx][ny])] = 0

dfs(0, 0, 1)
print(answer)