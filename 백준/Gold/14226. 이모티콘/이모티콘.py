import sys
from collections import deque
input = sys.stdin.readline
s = int(input())
visited = [[False] * (s + 1) for _ in range(s + 1)]
queue = deque()
queue.append((1, 0, 0))
visited[1][0] = True

while queue:
  emoji, clipBoard, time = queue.popleft()
  if emoji == s:
    print(time)
    break

  if not visited[emoji][emoji]:
    visited[emoji][emoji] = True
    queue.append((emoji, emoji, time + 1))
    
  if clipBoard > 0 and emoji + clipBoard <= s and not visited[emoji + clipBoard][clipBoard]:
    visited[emoji + clipBoard][clipBoard] = True
    queue.append((emoji + clipBoard, clipBoard, time + 1))
    
  if emoji - 1 >= 0 and not visited[emoji - 1][clipBoard]:
    visited[emoji - 1][clipBoard] = True
    queue.append((emoji - 1, clipBoard, time + 1))