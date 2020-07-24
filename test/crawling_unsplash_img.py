# crawling of unsplash img
# keyword is 카페
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlretrieve
from selenium import webdriver
import sys
import io
import time

# for printing korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

# input keyword
search_keyword = "cafe"
# string formatting
url = f"https://unsplash.com/s/photos/{quote_plus(search_keyword)}"

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(3)
driver.get(url)
html = driver.page_source
bs = BeautifulSoup(html, "html.parser")

# scroll reaction
# max 400 collect
# for i in range(100):
#     driver.execute_script("window.scrollBy(0, 1000)")
#     time.sleep(1)


# find tags which class name is .rg_i.Q4LuWd
img = bs.select("._2VWD4")

imgurl = []

# only crawling src attributes
for i in img:
    imgurl.append(i.get("src"))

n = 1
# save as other name
for i in imgurl:
    urlretrieve(i, "C:/cafe-img/unsplash/" + search_keyword + str(n) + ".jpg")
    n += 1
    # if n is 600:
    #     break

# termination
driver.close()

