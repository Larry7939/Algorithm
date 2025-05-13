# -39, -37, -29, -28, -6, 2, 11  
# 22 + 12 + 58 + 39
# 92 + 39
# 131

# -1, 3, 4, 5, 6, 11
# 가장 먼 곳에 있는 책을 가장 나중에 가져다 놓는 것이 핵심
# 11 + 10 + 6 + 2 => 29
# 가장 먼 곳에 있는 건 무조건 1번만.
# 가장 먼 곳에 있는 것부터 차례대로 M만큼 묶어서 계산하기

# 음의 배열과 양의 배열별로 단위별로 나눈다
# 각각을 새로운 배열에 절대값 형태로 넣는다.
# 제일 큰 것을 제외하고 나머지는 전부 곱하기 2를 해서 합한다.
n,m = map(int,input().split())
s = list(map(int,input().split()))
a = []
b = []
for i in s:
    if i < 0:
      a.append(i)  
    elif i > 0:
      b.append(i)
a.sort()
aLength = len(a)
b.sort(reverse=True)
bLength = len(b)
plusList = []
minusList =[]
result = 0
plusMax = 0
minusMax = 0
for i in range(0, aLength, m):
    minusList.append(abs(a[i]))
if len(minusList) != 0:
    minusMax = max(minusList)

for i in range(0, bLength, m):
    plusList.append(abs(b[i]))
if len(plusList) != 0:
    plusMax = max(plusList)

result += sum(plusList + minusList) * 2
result -= max(minusMax, plusMax)
print(result)
