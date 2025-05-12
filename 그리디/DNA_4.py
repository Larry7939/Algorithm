N, M = map(int,input().split())

result = ""
strings = []
for _ in range(N):
    strings.append(input())
diffSum = 0
# dict와 value 정렬을 활용하여, 각 인덱스 별로 가장 많이 언급된 것을 출력한다.
for i in range(M):
    s = ""
    counts = {'A':0, 'C':0, 'G':0, 'T':0}
    
    for j in range(N):
        s += strings[j][i]

    for dna in s:
        counts[dna] += 1
    counts = sorted(counts.items(), key= lambda x:x[1], reverse=True)
    result += counts[0][0]
    
    for k in range(1,4): # 가장 많은 것 제외 나머지 알파벳들의 합(Hamming Distance)
        diffSum += counts[k][1]

print(result)
print(diffSum)