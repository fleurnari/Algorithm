import sys
import math
input = sys.stdin.readline
n = int(input())
l, r = 0, n
answer = 0

while l <= r:
    mid = (l + r) // 2
    if mid * mid >= n:
        answer = mid
        r = mid - 1
    else:
        l = mid + 1

print(answer)