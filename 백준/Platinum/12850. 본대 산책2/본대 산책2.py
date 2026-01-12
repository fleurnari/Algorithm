import sys
input = sys.stdin.readline
d = int(input())
graph = [[0] * 8 for i in range(8)]
mod = 1000000007

graph[0][1] = graph[0][2] = 1
graph[1][0] = graph[1][2] = graph[1][3] = 1
graph[2][0] = graph[2][1] = graph[2][3] = graph[2][4] = 1
graph[3][1] = graph[3][2] = graph[3][4] = graph[3][5] = 1
graph[4][2] = graph[4][3] = graph[4][5] = graph[4][7] = 1
graph[5][3] = graph[5][4] = graph[5][6] = 1
graph[6][5] = graph[6][7] = 1
graph[7][4] = graph[7][6] = 1

def mul(a, b):
  result = [[0] * 8 for i in range(8)]
  for i in range(8):
    for j in range(8):
      for k in range(8):
        result[i][j] += a[i][k] * b[k][j]
      result[i][j] %= mod
  return result

def cal(a, n):
  if n == 1:
    return a
  tmp = cal(a, n // 2)
  if n % 2 == 0:
    return mul(tmp, tmp)
  else:
    return mul(mul(tmp, tmp), a)

answer = cal(graph, d)
print(answer[0][0])