# crawling of google img
# keyword is 카페
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlretrieve
from selenium import webdriver
import sys
import io

# for printing korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

# input keyword
search_keyword = input("검색어를 입력하세요 : ")
# string formatting
url = f"https://www.google.com/search?q={quote_plus(search_keyword)}&sxsrf=ALeKk01Kf9wYcHp9ra4r0mAha2cwUxXj3w:1593326226702&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi7zYPe8qPqAhXWdXAKHU9-BNwQ_AUoAnoECA4QBA&biw=1920&bih=1036"

driver = webdriver.Chrome("D:/chromedriver.exe")
driver.get(url)
html = driver.page_source
bs = BeautifulSoup(html, "html.parser")

# scroll reaction
# max 400 collect
for i in range(500):
    driver.execute_script("window.scrollBy(0, 10000)")

# find tags which class name is .rg_i.Q4LuWd
img = bs.select(".rg_i.Q4LuWd")

imgurl = []

# only crawling src attributes
for i in img:
    try:
        imgurl.append(i.attrs["src"])
    except KeyError:
        imgurl.append(i.attrs["data-src"])

n = 1
# save as other name
for i in imgurl:
    urlretrieve(i, "D:/cafe-crawling/" + search_keyword + str(n) + ".jpg")
    n += 1
    if n is 600:
        break

# termination
driver.close()

