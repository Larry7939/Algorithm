students = [0]*23

n = int(input())
a = map(int,input().split())

for i in a:
    students[i-1]+=1

print(*students)