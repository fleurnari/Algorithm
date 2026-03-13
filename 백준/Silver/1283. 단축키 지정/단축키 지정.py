import sys
input = sys.stdin.readline
n = int(input())
used = set()

for _ in range(n):
    s = list(input().rstrip())

    for i in range(len(s)):
        if (i == 0 or s[i - 1] == ' ') and s[i] != ' ' and s[i].lower() not in used:
            used.add(s[i].lower())
            s[i] = '[' + s[i] + ']'
            break

    else:
        for i in range(len(s)):
            if s[i] != ' ' and s[i].lower() not in used:
                used.add(s[i].lower())
                s[i] = '[' + s[i] + ']'
                break

    print(''.join(s))