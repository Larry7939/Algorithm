from collections import defaultdict

name_dict = defaultdict(int) #defaultdict 객체의 기본 형식으로 int를 지정한다.
name_dict['Bob'] = 1
name_dict['Katie'] = 2
sara_number = name_dict['Sara'] #원래 dict와는 달리, 존재하지 않는 키값으로 탐색을 해도 key error가 발생하지 않고, 0을 반환한다.
print(name_dict.get('Sara',0)) #원래 dict에서는 이렇게 해야 key error를 피할 수 있다.

# 위 코드에서 defaultdict의 기본 형식으로 int 대신 list를 지정하면, 즉 names_dict = defaultdict(list)로 바꿔 주면 “Sara”의 값은 아래와 같이 0 대신 빈 list가 할당된다.
# defaultdict(<class 'list'>, {'Bob': 1, 'Katie': 2, 'Sara': []})
# 마찬가지로, 기본 형식으로 dict로 지정하면 “Sara”의 값은 {}가 된다.

