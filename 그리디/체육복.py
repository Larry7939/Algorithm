# 프로그래머스 - 체육복
def solution(n, lost, reserve):
    # lost - 체육복을 도난당한 학생 번호
    # reserve - 여벌의 체육복이 있는 학생 번호

    # 여벌의 체육복을 가져왔지만 도난당한 경우를 고려
    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]

    # 테스트 케이스 중, 학생 번호가 정렬되지 않은 경우가 있음
    _lost.sort()
    _reserve.sort()

    for r in _reserve:
        if r-1 in _lost:
            _lost.remove(r-1)
        elif r+1 in _lost:
            _lost.remove(r+1)

    return n - len(_lost)
