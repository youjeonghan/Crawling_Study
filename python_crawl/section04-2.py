# Section04-2
# Requests
# request 사용 스크랩핑(2) - JSON

import json
import requests

s = requests.Session()

# 100개 JSON 데이터 요청
# stream=True로 옵션을 주면 좋다
r = s.get("https://httpbin.org/stream/100", stream=True)

# 수신 확인
print(r.text)

# Encoding 확인
print("Before Encoding : {}".format(r.encoding))

if r.encoding is None:
    r.encoding = "UTF-8"

print("After Encoding : {}".format(r.encoding))