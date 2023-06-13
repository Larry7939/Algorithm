import sys
n = sys.stdin.readline().rstrip()
half_length = len(n)//2
front_sum = 0
behind_sum = 0
for i in range(half_length):
    front_sum += int(n[i])
    behind_sum += int(n[half_length+i])

if front_sum == behind_sum:
    print("LUCKY")
else:
    print("READY")