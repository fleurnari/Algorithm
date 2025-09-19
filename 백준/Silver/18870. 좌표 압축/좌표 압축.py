import sys
input = sys.stdin.readline
n = int(input())
x = list(map(int, input().split()))
sortSet = sorted(list(set(x)))
dic = {sortSet[i] : i for i in range(len(sortSet))}

for i in x:
  print(dic[i], end = ' ')