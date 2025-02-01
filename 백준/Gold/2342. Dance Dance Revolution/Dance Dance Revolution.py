import sys
input = sys.stdin.readline
dpTable = [[[sys.maxsize for k in range(5)] for j in range(5)] for i in range(100001)]
powerList = [[0, 2, 2, 2, 2], [2, 1, 3, 4, 3], [2, 3, 1, 3, 4], [2, 4, 3, 1, 3], [2, 3, 4, 3, 1]]
n = 1
dpTable[0][0][0] = 0
inputList = list(map(int, input().split()))
idx = 0
result = sys.maxsize

while inputList[idx] != 0:
    tmp = inputList[idx]
    for i in range(5):
        if tmp == i:
            continue
        for j in range(5):
            dpTable[n][i][tmp] = min(dpTable[n - 1][i][j] + powerList[j][tmp], dpTable[n][i][tmp])
            
    for j in range(5):
        if tmp == j:
            continue
        for i in range(5):
            dpTable[n][tmp][j] = min(dpTable[n - 1][i][j] + powerList[i][tmp], dpTable[n][tmp][j])
    n += 1
    idx += 1
    
n -= 1

for i in range(5):
    for j in range(5):
        result = min(result, dpTable[n][i][j])
        
print(result)
