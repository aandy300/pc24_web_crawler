import requests
from bs4 import BeautifulSoup
import json

url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=ssd&page=1&sort=sale/dc"
res = requests.get(url) #pchome F12 Request Method: GET
data = json.loads(res.text) #json格式化 方便閱讀

data #檢視用

webdata = data['prods']

len (webdata) #pchome 單頁捲動式是 20筆資料

for product in webdata :
    print(product['name'])
    print(product['price'])

# for loop 做的事情 單次化
webdata #檢視用
webdata[1] #檢視用
x = webdata[1]
print(x['name'])
print('***************')
# ------------ 測試用

for product in webdata :
    print(product)
    print('-------------')