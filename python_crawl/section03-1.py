# Section03-1
# 기본 스크랩핑 실습
# Get 방식 데이터 통신(1)

import urllib.request
from urllib.parse import urlparse

# 기본 요청 1(encar)
url = "http://www.encar.com"

mem = urllib.request.urlopen(url)

# 여러 정보
print(f"type : {type(mem)}")
print(f"geturl : {mem.geturl()}")
print(f"status : {mem.status}")
print(f"hraders : {mem.getheaders()}")
print(f"getcode : {mem.getcode()}")
print(f"read : {mem.read(100).decode('utf-8')}")
print(f"parse : {urlparse('http://www.encar.co.kr?test=test').query}")