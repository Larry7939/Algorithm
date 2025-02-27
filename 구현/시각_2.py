# N, K

# N을 받고, N시 59분 59초를 초 단위로 변경 -> totalSecond
# 0부터 totalSecond까지 반복문으로 1씩 증가
# 매번 시분초 포맷 문자열로 변환한 후, K가 포함된 수를 세어서 result에 합산

# toSecond
def toSecond(timeFormat:str) :
    result = 0
    hour,minute,sec = map(int,timeFormat.split(":"))
    result += sec
    result += minute * 60
    result += hour * 60 * 60
    return result

# toTimeFormat 00:00:00
def toTimeFormat(second:int):
    hour = second // 3600
    minute = (second % 3600) // 60
    sec = (second % 3600) % 60
    result = ("%02d:%02d:%02d" %(hour, minute, sec))
    return result


# 입력
N, K = map(int,input().split())
result = 0
# 반복문
formattedTime = ("%02d" %N)+":59:59"
second = toSecond(formattedTime)

for sec in range(0, second+1):
    if str(K) in toTimeFormat(sec):
        result += 1
print(result)