import sys
n = list(map(int,sys.stdin.readline().rstrip()))
diffIndex = []
#앞뒤가 달라지는 인덱스 i를 배열 diffIndex에 append
for i in range(1,len(n)):
    if n[i-1] != n[i]:
        diffIndex.append(i)

print(diffIndex)
print(len(diffIndex)//2)
#[3,5,7,9]
#001101
#0101111100000100
#0010001001010 -> 4
#1111011110 -> 1
#010101010 -> 4