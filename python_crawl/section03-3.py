# Section03-3
# 기본 스크랩핑 실습
# 다음 주식 정보 가져오기

import json
import urllib.request as req
from fake_useragent import UserAgent

# Fake Header 정보 (가상으로 User-agent 생성)
ua = UserAgent()
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random)

# 헤더 정보
headers = {
    "User-agent": ua.ie,
    "referer": "https://finance.daum.net/",
}

# 다음 주식 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode("UTF-8")

# 응답 데이터 확인 (Json Data)
# print("res", res)

# 응답 데이터 str -> json 변환 및 data 값 출력
rank_json = json.loads(res)["data"]

# 중간 확인
# print("중간 확인 : ", rank_json, "\n")

for elm in rank_json:
    # print(type(elm))
    print("순위 : {}, 금액 : {}, 회사명 : {}\n".format(elm["rank"], elm.get("tradePrice"), elm["name"]))
    # 파일 (csv, 엑셀, txt) 저장 및 db 저장