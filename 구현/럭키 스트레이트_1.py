import sys
n = sys.stdin.readline().rstrip()
half_length = len(n)//2
front = n[:half_length]
behind = n[half_length:]
front_sum = 0
behind_sum = 0
front_sum = sum([int(x) for x in front])
behind_sum = sum([int(y) for y in behind])
if front_sum == behind_sum:
    print("Lucky")
else:
    print("Ready")