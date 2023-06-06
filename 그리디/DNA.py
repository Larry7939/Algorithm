#BOJ 1969 DNA
import sys
n,m = map(int,sys.stdin.readline().split())
dna_list = []
result = ""
min_distance = 0
for _ in range(n):
    dna_list.append(sys.stdin.readline().rstrip())
def initCount():
    global a_count, c_count, g_count, t_count
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
#각 dns s의 열에서 가장 등장 빈도가 높은 것들로 s를 구성

a_count = 0
c_count = 0
g_count = 0
t_count = 0

for i in range(m):
    for j in range(n):
        a_count += dna_list[j][i].count('A')
        c_count += dna_list[j][i].count('C')
        g_count += dna_list[j][i].count('G')
        t_count += dna_list[j][i].count('T')
    if max(a_count,c_count,g_count,t_count) == a_count:
        result += 'A'
        min_distance += c_count + g_count + t_count #hemming distance 세기(가장 빈도가 높은 알파벳 개수를 제외한 나머지를 더함)
    elif max(a_count,c_count,g_count,t_count) == c_count:
        result += 'C'
        min_distance += a_count + g_count + t_count
    elif max(a_count,c_count,g_count,t_count) == g_count:
        result += 'G'
        min_distance += c_count + a_count + t_count
    elif max(a_count,c_count,g_count,t_count) == t_count:
        result += 'T'        
        min_distance += c_count + g_count + a_count
    initCount()


print(result)
print(min_distance)
