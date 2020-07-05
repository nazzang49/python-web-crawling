# crawling of bing img
# keyword is 카페
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlretrieve, urlopen
from selenium import webdriver
import time
import sys
import io

# for printing korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

# input keyword
search_keyword = input("검색어를 입력하세요 : ")
# string formatting
url = f"https://www.bing.com/images/search?q={quote_plus(search_keyword)}&form=HDRSC2&first=1&scenario=ImageBasicHover"

driver = webdriver.Chrome("D:/chromedriver.exe")
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
html = driver.page_source
bs = BeautifulSoup(html, "html.parser")

for i in range(500):
    driver.execute_script("window.scrollBy(0, 10000)")

time.sleep(5)

# find tags which class name is .mimg
img = bs.find_all("img", class_="mimg")

imgurl = []
# only crawling src attributes
for i in img:
    try:
        imgurl.append(i.attrs["src"])
    except KeyError:
        imgurl.append(i.attrs["data-src"])

n = 1
for i in imgurl:
    urlretrieve(i, "D:/cafe-crawling-bing/" + search_keyword + str(n) + ".jpg")
    n += 1

# termination
driver.close()

