import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
arr = [0] * n

for i in range(n):
  arr[i] = int(input())

arr.sort()

print(round(sum(arr) / n))
print(arr[n // 2])
mostVal = Counter(arr).most_common()
if len(mostVal) > 1 and mostVal[0][1] == mostVal[1][1]:
  print(mostVal[1][0])
else:
  print(mostVal[0][0])
print(max(arr) - min(arr))