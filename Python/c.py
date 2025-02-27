# 소셜 미디어 상에서 친구일 가능성이 가장 높은 유저를 친구로 추천하는 기능을 만들려 한다.
# 이 때, 친구가 아닌 유저 중 mutual firend가 많을 수록 친구일 가능성이 높다고 본다.
# 예를 들어, 친구 관계가 다음과 같다면,
# david와 frank가 친구
# demi와 david가 친구
# frank와 james가 친구
# demi와 james가 친구
# claire와 frank가 친구
# - david와 james의 mutual friend는 2명(frank와 demi)
# - david와 claire의 mutual firend는 1명(frank)
# 이므로, david와 친구일 가능성이 가장 높은 유저는 james이다. (이미 david와 친구인 frank와 demi는 추천 대상이 아니다.)
# 소셜 미디어 상에서 친구 관계를 담은 리스트 friends와 친구 추천 대상의 아이디 user_id가 주어질 때, 누구를 친구로 추천해야하는지 구하는 함수 solution을 완성하라.

# - friend는 길이가 10,000 이하인 리스트이다.
# - friend의 원소는 [x,y] 형태이며, 이는 아이디가 x인 유저와 아이디가 y인 유저가 소셜 미디어상에서 친구라는 의미이다.
# - x와 y는 길이가 1 이상 20이하인 소문자 문자열이다.
# - 동일한 친구 관계가 중복해서 주어지지 않는다.
# - user_id는 길이가 1이상 20이하인 소문자 문자열이다.
# - 친구가 없는 유저는 없다.
# - 따라서 firends에서 적어도 한 번은 나오는 아이디가 user_id로 주어진다.
# - 모든 유저 아이디는 알파벳 소문자로만 이루어져있다.
# - 친구일 가능성이 가장 높은 유저가 여럿일 경우, 유저의 id를 오름차순으로 정렬해 리턴한다.
# -  mutual firend가 한 명도 없는 경우는 주어지지 않는다.

# 입출력 예시
# friends = [["david","frank"], ["demi","david"], ["frank", "james"], ["demi","james"], ["claire", frank"]]
# user_id = "david"
# return ["james"]

from collections import defaultdict

# 키 포인트 : 친구의 친구 찾기
def solution(friends, user_id):
    # 친구 관계를 그래프 형태로 저장
    graph = defaultdict(set)
    for friend in friends:
        graph[friend[0]].add(friend[1])
        graph[friend[1]].add(friend[0])

    # user_id의 모든 친구와의 mutual firend 찾기
    mutual_friends = defaultdict(int)
    for friend in graph[user_id]:
        for mutual_friend in graph[friend]:
            # 본인이 아니고 이미 친구 관계인 인물이 아닌 경우에 한하여 mutual firend 추가
            if mutual_friend != user_id and mutual_friend not in graph[user_id]:
                mutual_friends[mutual_friend] += 1

    # mutual firend가 가장 많은 유저 찾기
    max_count = max(mutual_friends.values())
    recommended_users = [user for user, count in mutual_friends.items() if count == max_count]
    print(recommended_users)
    # 친구일 가능성이 가장 높은 유저들을 오름차순으로 정렬하여 반환
    return sorted(recommended_users)

# 예시 입력
friends = [["david","frank"], ["demi","david"], ["frank", "james"], ["demi","james"], ["claire", "frank"]]
user_id = "david"

# 함수 호출 및 결과 출력
solution(friends, user_id)  # ["james"]