# section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 url
img_url = "https://newsimg.hankookilbo.com/cms/articlerelease/2019/04/29/201904291390027161_3.jpg"
html_url = "https://google.com"

# 다운 받을 경로
save_path1 = "c:/Users/win7/Documents/GitHub/Crawling_Study/save_folder/test1.jpg"
save_path2 = "c:/Users/win7/Documents/GitHub/Crawling_Study/save_folder/index.html"

# 예외 처리
# urlretrieve함수는 파일이름, 수신 헤더값 2개 반환 (다운로드하는 함수임 (파일url, 다운받을 파일 경로))
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print("Download failed")
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print("Filename1 {}".format(file1))
    print("Filename2 {}".format(file2))
    print()

    # 성공
    print("Download Sucessed")
