import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
matrix = []
matrix.append((0, 0))
dpTable = [[-1 for j in range(n + 1)] for i in range(n + 1)]

for i in range(n):
    r, c = map(int, input().split())
    matrix.append((r, c))
    
def matMul(s, e):
    result = sys.maxsize
    if dpTable[s][e] != -1:
        return dpTable[s][e]
    if s == e:
        return 0
    if s + 1 == e:
        return matrix[s][0] * matrix[e][0] * matrix[e][1]
    for i in range(s, e):
        result = min(result, matrix[s][0] * matrix[i][1] * matrix[e][1] + matMul(s, i) + matMul(i + 1, e))
    dpTable[s][e] = result
    return dpTable[s][e]

print(str(matMul(1, n)))