import sys
input = sys.stdin.readline
n, m = map(int, input().split())
groupToMembers = {}
memberToGroup = {}

for _ in range(n):
  group = input().strip()
  cnt = int(input())
  members = []
  for _ in range(cnt):
    member = input().strip()
    members.append(member)
    memberToGroup[member] = group
  groupToMembers[group] = sorted(members)

for _ in range(m):
  name = input().strip()
  type = int(input())
  if type == 0:
    for member in groupToMembers[name]:
      print(member)
  else:
    print(memberToGroup[name])