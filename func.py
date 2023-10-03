numbers = [1, 2, 3, 4, 5]

# max(numbers)
# max(1,2,3,4,5)와 동일한 의미

max_num = max(numbers)
# print(max_num)

#######

import random

random_number = random.randint(1, 100)
# random이라는 박스 안의 randint라는 도구를 꺼낸다는 의미로 해석
# 1부터 100 사이의 무작위 정수를 random_number로 지정한다는 의미

#######

menus = ['김밥', '라면', '만두']
random_number = random.randint(0,2)
# print(menus[random_number])

menu = random.choice(menus)
# print(menu)

#######

numbers = range(1, 46) # 1이상 46미만의 범위
lucky_number = random.choice(numbers)
# lucky_number를 6번 추출하게되면 중복이 있을 수 있음

lucky_number = random.sample(numbers, 6) 
# numbers에서 6개의 숫자를 뽑겠단 의미

# print(lucky_number)
# 무작위로 선별된 6개의 숫자가 순서 상관없이 출력됨
# print(sorted(lucky_number))
# 6개의 숫자가 정렬되어 출력됨

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086'

# pip install requests
import requests

res = requests.get(URL)

data = res.json()

drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

# print(drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6) 

# print(data['drwNoDate'])

lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

print(lucky_number)
print(lotto_number)

print(set(lucky_number) & set(lotto_number))
# set() & set() 은 교집합 찾는 함수