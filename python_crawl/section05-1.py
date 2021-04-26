# Section05-1
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(1) - 기본 사용법

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <h1>this is h1 area</h1>
        <h2>this is h2 area</h2>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sistes.
            <a href="http://example.com/elsie" class="sister" id ="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id ="link2">Lacie</a>
            <a data-io="link3" href="http://example.com/little" class="sister" id ="link1">Title</a>
        </p>
        <p class="story">
            story...
        </p>
    </body>
</html>
"""