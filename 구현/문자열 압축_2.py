# 프로그래머스 - 문자열 압축 100/100
def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s)//2)+1):
        result = ''
        cnt = 1
        before = s[:i] # 미리 첫번째 단위 끊어놓기

        for j in range(i, len(s), i):
            now = s[j:j+i]
            if before == now: # 현재 단위와 비교 후, 일치하면 cnt+=1
                cnt += 1
            else: # 불일치한 경우
                if cnt != 1: # 앞에서 연속된 단위가 있었다면,
                    result = result + str(cnt) + before # 해당 단위로 문자열 압축
                else:
                    result = result + before
                before = now # 현재 단위 저장(연속될 땐 해줄 필요 없음)
                cnt = 1 # cnt 초기화

        # 마지막이 연속한 단위로 끝나버려서 else문에 들어가지 않아 압축될 기회가 없는 경우를 대비
        if cnt != 1:
            result = result + str(cnt) + before
        else:
            result = result + before
        # 매 단위마다 압축한 길이를 append
        answer.append(len(result))
    return min(answer)

#매번 단위를 높여가며, 연속되는 문자열을 체크하는 것이 핵심