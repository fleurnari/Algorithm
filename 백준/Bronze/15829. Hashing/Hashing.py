import sys
input = sys.stdin.readline
l = int(input())
strList = list(str(input().strip()))
answer = 0

for i in range(len(strList)):
  answer += (ord(strList[i]) - 96) * (31 ** i)
 
print(answer % 1234567891)