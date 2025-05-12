# 프로그래머스 - 문자열 압축 100/100
# 1부터 len(s)//2+1까지 step을 증가시켜가며 점점 큰 단위로 나눠간다.
# step loop
# 문자열 loop:
#  첫번째 원소는 before로 해놓고, 
#  문자열 완성 -> count와 문자열을 붙여 완성하는 과정 ex) aaa -> 3a
#  
#  문자열을 완성시키는 시점: 다음으로 가서 before와 now가 다를 때마다 완성
# 한 step이 끝날 때마다 s-key, length-value로 하는 dict에 저장한다.
# 오름차순으로 정렬 후 맨 앞 원소의 value를 출력

def solution(s):
    if len(s) == 1:
        return 1
    answer = []
    n = len(s)
    half_length = n//2
    for step in range(1, half_length+1):
        result = ""
        before = s[:step]
        count = 1
            
        for i in range(step, n, step):
            now = s[i:i+step]

            #같은 경우에는, 공통된 단위로 묶을 수 있기 때문에, count += 1을 해줘야함                             
            if before == now:
                count += 1
            # 만약 before와 now가 다른 경우, 문자열 완성시켜주고 count를 1로 초기화 해줘야함. ex) aab-> 2ab
            # 다만, 문자가 반복되지 않는 경우, 즉, count가 1인 경우에는 count를 생략한다.
            else:
                if count > 1:
                    result = result + str(count) + before 
                elif count == 1:
                    result = result + before
                count = 1
                    
            
                before = now
        # 마지막인 경우에는 문자열 완성 시켜주기
        if count > 1:
            result = result + str(count) + before
        else:
            result = result + before
        answer.append(len(result))
    return min(answer)