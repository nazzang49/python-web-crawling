from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlretrieve, urlopen
from selenium import webdriver
import sys
import io

# for printing korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

# input keyword
search_keyword = input("검색어를 입력하세요 : ")
# string formatting
url = f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={quote_plus(search_keyword)}"

driver = webdriver.Chrome("D:/chromedriver.exe")
driver.get(url)
html = driver.page_source
bs = BeautifulSoup(html, "html.parser")

# scroll reaction
# max 400 collect
for i in range(500):
    driver.execute_script("window.scrollBy(0, 500)")

# find tags which class name is .rg_i.Q4LuWd
img = bs.find_all(class_="_img")

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('D:/deep_learning_model-crawling-naver/' + search_keyword + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)

# termination
driver.close()

