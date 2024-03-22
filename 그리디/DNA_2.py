from collections import Counter
# DNA의 수 N
# 문자열의 길이 M
# dnas
N, M = map(int,(input().split()))

# 각 DNA들의 같은 위치의 원소들 중 가장 많은 수를 차지하는 알파벳을 선정해야한다.
# 맨 앞부터 검사하면서 dict 형태로 
# 맨 앞부터 검사하면서 가장 많이 등장한 알파벳 append
# N-가장 많이 등장한 알파벳의 등장 수를 HammindDistance에 더해준다.
colum = [[] for _ in range(M)]
result_dna = []
hamming_distance = 0
for i in range(N):
    dna = input()
    for j in range(M):
        colum[j].append(dna[j])
for i in range(M):
    most_common_char = Counter(sorted(colum[i])).most_common(1)[0]
    result_dna.append(most_common_char[0])
    hamming_distance += N-most_common_char[1]
print("".join(result_dna))
print(hamming_distance)
    
# Hamming Distance의 합이 가장 작은 DNA 출력
# Hamming Distance의 합 출력
# 동일하다면 사전순으로 앞서는 것 출력