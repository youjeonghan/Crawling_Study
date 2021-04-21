# https://lostark.game.onstove.com/Market/GetMarketItemList?firstCategory=0&secondCategory=0&characterClass=&tier=0&grade=99&itemName=%EC%A7%84%EC%A3%BC&pageSize=10&pageNo=1&isInit=false&sortType=7&_=1618972050345

import requests

url = "https://lostark.game.onstove.com/Market/GetMarketItemList?firstCategory=0&secondCategory=0&characterClass=&tier=0&grade=99&itemName=%EC%A7%84%EC%A3%BC&pageSize=10&pageNo=1&isInit=false&sortType=7&_=1618972050345"
response = requests.get(url)
print(response.text)