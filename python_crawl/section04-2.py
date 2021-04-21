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
# print(r.text)

# Encoding 확인
print("Before Encoding : {}".format(r.encoding))

if r.encoding is None:
    r.encoding = "UTF-8"

print("After Encoding : {}".format(r.encoding))

for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인
    # print(line)
    # print(type(line))

    # JSON(Dict) 변환 후 타입 확인
    b = json.loads(line)  # str -> dict
    # print(b)
    # print(type(b))

    # 정보 내용 출력
    for k, v in b.items():
        print(f"Key : {k}, value : {v}")

    print("\n")

s.close()

# -----------------------------------------

r = s.get("https://jsonplaceholder.typicode.com/todos/1")

# Header 정보
# print(r.headers)

# 본문 정보
print(r.text)

# json 변환
print(r.json())

# key 반환
print(r.json().keys())

# value 반환
print(r.json().values())

# 인코딩 반환
print(r.encoding)

# 바이너리 정보
print(r.content)

s.close()