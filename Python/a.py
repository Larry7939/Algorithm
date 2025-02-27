# 알파벳이 적힌 카드 24장이 한 줄에 8장씩, 세 줄로 놓여있다.
# 같은 알파벳이 적힌 카드가 여러장 있을 수 있으나, 같은 알파벳이 적힌 카드는 반드시 같은 줄에 놓여있다.
# 알파벳과 어떤 단어들이 입력값으로 주어질 때, 각 단어를 주어진 카드로 만들 수 있는지를 판별하려고 한다. 단, 주어진 카드로 만들 때에는 반드시 한 줄에 한 카드는 사용해야한다.
# 예를 들어서 주어진 단어가 ["GPQM", "GPMZ", "EFU", "MMNA"인 경우,
# GPQM이라는 단어는 첫번째 줄에서 G, 두번째 줄에서 P와 Q, 세번째 줄에서 M을 골라 만들 수 있다.
# GPMZ라는 단어는 Z가 적힌 카드가 없으므로 만들 수 없다.
# EFU라는 단어는 첫번째 줄에서 E와 F, 두번째 줄에서 U를 고르면 완성이 되지만, 세번째 줄의 카드를 사용하지 않았기 때문에 단어를 만들수 없다.
# MMNA라는 단어는 세번째 줄에서 M 2개, 두번 째 줄에서 N, 첫번째 줄에서 A를 골라서 만들 수 있다.
# 알파벳이 적힌 카드 card와 만들어야하는 단어들 word가 매개변수로 주어질 때, 만들 수 있는 단어들만 return하는 solution함수를 완성해주세요.
# 단, 만들 수 있는 단어들을 return할 때는 매개변수 word의 순서대로 반환하면 된다.
# 위의 예시에서는 ["GPQM", "MMNA"]로 반환하면 된다.
# 또한, 어떤 단어도 만들 수 없는 경우에는 1차원 배열에 "-1"을 넣어 반환하면 된다.

# card는 길이가 3인 1차원 배열이고, card의 원소는 길이가 8인 string형이다. 이 문자열을 대문자로만 이루어져있다.
# word는 1차원 배열로 주어지며, 배열의 길이는 10이하의 자연수인다.
# word의 각 원소는 string이며, 각 원소의 길이는 24이하의 자연수이다.

# word는 1차원 배열, 배열의 길이는 10이하 자연수
# word의 각 원소는 string이고, 각 원소의 길이는 24이하의 자연수
# card는 길이가 3인 1차원 배열
# card의 원소는 길이 8의 string형이고 전부 대문자.

# 시간 복잡도: O(1)
def solution(card, word):
    # 결과 리스트 answer
    answer = []

    # 각 단어에 대해 확인
    for w in word: # O(10)
        # 세 줄에서 필요한 문자를 저장할 리스트
        needed = [[], [], []]
        
        # 단어의 각 문자에 대해 확인
        for char in w: # O(24)
            # 문자가 어느 줄에 있는지 확인하고 해당 줄의 필요한 문자 리스트에 추가
            for i in range(3): # O(3)
                if char in card[i]:
                    needed[i].append(char)
                    break

        # 1. all(needed) -> needed의 요소 리스트들이 비어있지 않은지 확인 -> 각 줄에서 문자를 하나라도 사용했는지 확인 -> 만약 한 줄에서라도 사용하지 않은 경우에는 단어를 만들 수 없음.
        # 2. 각 줄에서 사용된 문자의 카운트 합과 단어의 길이를 비교하여 실제로 만들 수 있는 단어인지 확인
        if all(needed) and sum(len(lst) for lst in needed) == len(w):
            valid = True
            for i in range(3): # O(3)
                # 해당 줄에서 필요한 문자의 수를 카운트
                count = {char: needed[i].count(char) for char in set(needed[i])}
                # 카드에서 각 문자의 수가 충분한지 확인
                for char, cnt in count.items():
                    if card[i].count(char) < cnt:
                        valid = False
                        break
                if not valid:
                    break
            
            # 유효하면 결과 리스트에 단어 추가
            if valid:
                answer.append(w)

    # 결과가 비어 있으면 ["-1"]을 반환
    if not answer:
        return ["-1"]

    return answer

# 예시 입력1
card1 = ["ABACDEFG", "NOPQRSTU", "HIJKLKKMM"]
word1 = ["GPQM", "GPMZ", "EFU", "MMNA"]
print(solution(card1, word1))  # 출력: ["GPQM", "MMNA"]

# 예시 입력2
card2 = ["AABBCCDD", "KKKKJJJJ", "MOMOMOMO"]
word2 = ["AAAKKKKKMMMMM","ABCDKJ"]
print(solution(card2, word2))  # 출력: ["-1"]