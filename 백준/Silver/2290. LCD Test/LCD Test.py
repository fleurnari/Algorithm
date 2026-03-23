import sys
input = sys.stdin.readline
s, n = input().split()
s = int(s)
nums = {
    '0': [1,1,1,1,1,1,0],
    '1': [0,1,1,0,0,0,0],
    '2': [1,1,0,1,1,0,1],
    '3': [1,1,1,1,0,0,1],
    '4': [0,1,1,0,0,1,1],
    '5': [1,0,1,1,0,1,1],
    '6': [1,0,1,1,1,1,1],
    '7': [1,1,1,0,0,0,0],
    '8': [1,1,1,1,1,1,1],
    '9': [1,1,1,1,0,1,1],
}

def horizontal(on):
    return ' ' + ('-' * s if on else ' ' * s) + ' '

def vertical(left, right):
    return ('|' if left else ' ') + (' ' * s) + ('|' if right else ' ')

for digit in n:
    print(horizontal(nums[digit][0]), end=' ')
print()

for _ in range(s):
    for digit in n:
        print(vertical(nums[digit][5], nums[digit][1]), end=' ')
    print()

for digit in n:
    print(horizontal(nums[digit][6]), end=' ')
print()

for _ in range(s):
    for digit in n:
        print(vertical(nums[digit][4], nums[digit][2]), end=' ')
    print()

for digit in n:
    print(horizontal(nums[digit][3]), end=' ')
print()