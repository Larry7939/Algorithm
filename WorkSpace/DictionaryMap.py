d = {}
d['data'] = '자료'
d['structure'] = '구조'
d['sequential search'] = '선형탐색'
d['game'] = '게임'
d['binary search'] = '이진탐색'
print("나의 단어장:")
print(d)

if d.get('game'): print("탐색 game -->",d['game'])
if d.get('over'): print("탐색 over -->",d['over'])
if d.get('data'): print("탐색 data -->",d['data'])
d.pop('game')
print("나의 단어장")
print(d)