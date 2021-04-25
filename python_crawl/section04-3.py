# Section04-3
# Requests
# request 사용 스크랩핑(3) - Rest API

import requests

# Rest API : GET, POST, DELETE, PUT:UPDATA, REPLACE(FERTCH : UPDATA, MODIFY)
# 중요 : URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# ex) GET : www.moviegg.com/movies : 영화를 전부 조회
# ex) GET : www.moviegg.com/movies/id : id인 영화를 조회
# ex) POST : www.moviegg.com/movies/ : 영화를 생성
# ex) PUT : www.moviegg.com/movies/ : 영화를 수정
# ex) DELETE : www.moviegg.com/movies/ : 영화를 삭제

# 세션 활성화
s = requests.Session()

# 예제 1
r = s.get("https://api.github.com/events")

# 수신상태 체크
# 예외가 일어나면 예외처리 후 종료
r.raise_for_status()

# 출력
print(r.text)

# 예제2
# 쿠키 설정
jar = requests.cookies.RequestsCookieJar()
# 쿠키 삽입
jar.set("name", "youjeinghan", domain="httpbin.org", path="/cookies")

# 요청
r = s.get("http://httpbin.org/cookies", cookies=jar)

# 출력
print(r.text)

# 예제3
r = s.get("https://github.com", timeout=5)

# 출력
print(r.text)


# 예제4
r = s.post("http://httpbin.org/post", data={"id": "yjh9360", "pw": "1234"}, cookies=jar)

# 출력
print(r.text)
print(r.headers)


# 예제5
# 요청(POST)
# 튜플로도 가능
payload1 = {"id": "yjh9360", "pw": "12345678"}
payload2 = (("id", "yjh9360"), ("pw", "12345678"))

r = s.post("http://httpbin.org/post", data=payload2)

# 출력
print(r.text)


# 예제 6(PUT)
r = s.put("http://httpbin.org/put", data=payload1)

# 출력
print(r.text)


# 예제 7(DELETE)
r = s.delete("http://httpbin.org/delete", data={"id": 1})

# 출력
print(r.text)

# 예제 7_2(DELETE)
r = s.delete("https://jsonplaceholder.typicode.com/posts/1")

# 출력
print(r.ok)
print(r.text)
print(r.headers)

s.close