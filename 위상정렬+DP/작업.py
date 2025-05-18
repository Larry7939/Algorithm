# 풀이 횟수 2
from collections import deque

# 작업의 개수 입력
n = int(input())

# graph[i]: i번 작업이 완료된 후 수행 가능한 후속 작업 목록
graph = [[] for _ in range(n + 1)]

# in_degree[i]: i번 작업을 수행하기 전에 완료되어야 하는 선행 작업 수
in_degree = [0] * (n + 1)

# time[i]: i번 작업을 수행하는 데 걸리는 시간
time = [0] * (n + 1)

# dp[i]: i번 작업을 완료하는 데에 걸리는 최대 누적 시간
dp = [0] * (n + 1)

# 작업 정보 입력 처리
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]  # 첫 번째 값은 해당 작업 자체의 소요 시간
    for pre in data[2:]:  # 선행 작업 번호들
        graph[pre].append(i)      # pre 작업이 끝나야 i 작업을 시작할 수 있음
        in_degree[i] += 1         # i 작업의 진입 차수 증가 (선행 작업 수)

# 위상 정렬을 위한 큐 초기화
queue = deque()

# 선행 작업이 없는 작업들부터 시작 (진입 차수가 0인 작업)
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)
        dp[i] = time[i]  # 선행 작업이 없으므로, 소요 시간은 자기 자신만

# 위상 정렬 실행
while queue:
    now = queue.popleft()
    
    # 현재 작업(now)을 끝낸 후 수행할 수 있는 하위 작업들(next)을 순회
    for next in graph[now]:
        # 선행 작업(now)이 끝났을 때, next 작업이 시작할 수 있는 시간 후보
        # 기존 dp[next] 값과 비교해서 더 오래 걸리는 쪽을 선택
        # 다음 작업(next)가 완료될 때까지의 시간인 dp[next]에 영향을 줄 수 있는 작업이 여러 개일 수 있음.
        # 즉, 하위 작업의 상위 작업이 하나일 때에는 dp[next]가 0인데, 여러 개일 때에는 바뀔 수 있음
        # 경로에 따라 dp[next]는 달라질 수 있는 거니까.
        
        dp[next] = max(dp[next], dp[now] + time[next])
        
        # now 작업이 끝났으므로, next의 남은 선행 작업 수 감소
        in_degree[next] -= 1
        
        # 모든 선행 작업이 끝났다면 큐에 추가 (이제 수행 가능)
        if in_degree[next] == 0:
            queue.append(next)

# 모든 작업을 완료하는 데 걸리는 최소 시간은 dp 배열의 최댓값
print(max(dp))