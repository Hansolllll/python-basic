import requests
from pprint import pprint

URL = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2B58fRxySTvs0PfFQUY4WIxmfUdNzO2PRCGrFR%2BwurNXadOEb4nRyU4TfZFft%2FX7IOwZchblSbWUzs2S9mm1q2Q%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'

res = requests.get(URL)
# import requests 하지 않고 request.get 실행 시 에러발생

data = res.json() # json 형태의 데이터를 python에서 사용할 수 있는 딕셔너리 형태로 변환

# pprint(data) # pprint 함수 가져오기
# pprint는 pretty print 라는 의미
# 이 때 'response' - 'body' - 'item'의 계층을 가진 딕셔너리로 출력됨

items = data['response']['body']['items']
# 'response', 'body', 'items'를 추가로 기입할 때마다 하위로 이동
# 마지막 'items' 기입하면 딕셔너리->리스트 형태로 바뀜(인덱스 접근 필요)

for item in items:
    if item['stationName'] == '강남구':
        pprint(item['pm10Value'])
# 전체 데이터에서 강남구의 정보만 출력
