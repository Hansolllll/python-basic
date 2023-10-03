# 1. apple / Apple(대/소문자 구분)
# 2. git add. / git add .(띄어쓰기 확인) 
# 3. message / massage(오타 주의)         
 
# 1. 변수, variable

# 1 - 숫자(int)
dust = 10

# 2 - 글자(string)
dust = '5'

# 3 - 참/거짓(boolean)
dust = True # False

dust_list = [10, 20, 0, 50, 100]
# 대괄호는 여러개의 데이터를 나열 할 수 있는 '리스트'를 의미
# 리스트 안의 각 데이터에 접근하고 싶으면 데이터의 순번을 이용해야함(0부터 시작)
# print(dust_list[3])

dust_dict = {
    '서울': 100,
    '대전': 10,
    '부산': 50,
}
# 중괄호는 여러개의 key-value를 나열할 수 있는 '딕셔너리'를 의미
# 보통 여는 중괄호 - 공백(줄비움) - 닫는 중괄호 구조로 사용
# 콜론 앞은 붙이고 뒤는 띄어쓰기
# print(dust_dict['부산'])

# 2. 조건
age = 10

if age > 20:
    print('성인입니다.')
elif age > 8:
    print('청소년입니다.')
else:
    print('어린이입니다.')
 # 코드 실행 시 변수의 값과 조건에 따라 해당 값이 출력됨

dust = 30

# dust 150보다 크다면 => 매우나쁨
# 80~150 => 나쁨
# 30~79 => 보통
# 0~29 => 좋음
if dust <= 29:
    print('좋음')
elif dust <= 79:
    print('보통')
elif dust <= 150:
    print('나쁨')
else:
    print('매우나쁨')


# 3. 반복
menus = ['짜장면', '김치찌개', '김치찜', '아구찜']

n = 0
while n < 4:
    print(menus[n])
    n = n + 1
# while 조건에 부합하지 않는 순간 반복문이 종료됨
# 자주 사용하는 것은 아님

for menu in menus:
    print(menu)
# for item in list 형태로 쓰며 list 내부의 각 데이터를 item으로 이름 붙이고 list 내부 모든 데이터를 한번 프린트하고 멈추는 방식
# 알고리즘 외에 반복문은 주로 for문을 사용함
