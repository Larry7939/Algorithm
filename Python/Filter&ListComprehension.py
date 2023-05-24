a = [{'email': "google", 'gender': 'm'},
     {'email': "naver", 'gender': 'm'},
     {'email': "kakao", 'gender': 'y'},
     {'email': "hanmail", 'gender': 'm'}]
# result = list(filter(lambda user: user['gender'] == 'm', a))
result = [x['gender'] for x in a if x['gender']=='m']
print(result)

b = [10,2,3,4,5,6,7]
# def isBiggerThanFour(iterable):
#     return iterable > 4
# result = list(filter(isBiggerThanFour, b))
result = [x for x in b if x>4]
print(result)