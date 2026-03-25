import sys
input = sys.stdin.readline
n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]
left = 1
right = max(t) * m
answer = right

while left <= right:
    mid = (left + right) // 2
    total = 0

    for time in t:
        total += mid // time
        if total >= m:
            break

    if total >= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)