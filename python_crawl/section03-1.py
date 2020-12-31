# Section03-1
# 기본 스크랩핑 실습
# Get 방식 데이터 통신(1)

import urllib.request
from urllib.parse import urlparse

# 기본 요청 1(encar)
url = "http://www.encar.com"

mem = urllib.request.urlopen(url)

# 여러 정보
# urlparse가 도메인, 프로토콜, 쿼리 부분을 분리해줌
print(f"type : {type(mem)}")
print(f"geturl : {mem.geturl()}")
print(f"status : {mem.status}")
print(f"hraders : {mem.getheaders()}")
print(f"getcode : {mem.getcode()}")
print(f"read : {mem.read(100).decode('utf-8')}")
print(f"parse : {urlparse('http://www.encar.com?test=test').query}")

# 기본 요청 2(ipify)
API = "https://api.ipify.org"

# Get 방식 parameter
values = {"format": "json"}  # text, json, jsonp 등등 으로 가능

print(f"before param : {values}")
params = urllib.parse.urlencode(values)
print(f"before param : {params}")

# 요청 URL 생성
URL = API + "?" + params
print(f"요청 URL = {URL}")

# 수신 데이터 읽기
data = urllib.request.urlopen(URL).read()


# 수신 데이터 디코딩
text = data.decode("utf-8")
print(f"response : {text}")