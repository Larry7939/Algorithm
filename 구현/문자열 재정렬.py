import sys
s = sys.stdin.readline().rstrip()
alphabets = []
numbers = []
for i in s:
    if 65<= ord(i) <= 90:
        alphabets.append(i)
    else:
        numbers.append(i)
alphabets.sort()
numbers.sort()
answer = alphabets+numbers
for i in answer:
    print(i,end='')
