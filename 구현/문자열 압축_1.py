#프로그래머스 - 문자열 압축 62/100
def solution(s):
    half_length = len(s)//2
    answer = []
    
    for i in range(1,half_length+1): # 단위 설정
        before = s[0:i]
        count = 1
        dict_str = dict()
        for j in range(i,len(s)+i,i): # 설정된 단위 i로 압축
            now = s[j:j+i]
            if before == now:
                count += 1 
                dict_str[before] = count
            else:
                before = now
                count = 1
        #dict_str에 있는 것들 중에서 가장 value가 큰 key값
        if dict_str:
            max_value = max(dict_str.values())
            max_keys = [key for key,value in dict_str.items() if value == max_value]
            temp = s
            for key in max_keys:
                value = dict_str.get(key)
                temp = temp.replace(key*value,str(value)+key)
            answer.append(len(temp))

    if answer:
        return min(answer)
    else:
        return len(s)