import sys
input = sys.stdin.readline

while True:
    try:
        s, t = input().strip().split()
        idx = 0
    
        for char in t:
            if idx < len(s) and s[idx] == char:
                idx += 1
    
        if idx == len(s):
            print("Yes")
        else:
            print("No")
    except:
        break