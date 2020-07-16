# crawling of bing img
# keyword is 카페
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlretrieve, urlopen
from selenium import webdriver
import time
import sys
import io
import os

# for printing korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

# crawling img files referring to cafe themes
cafe_theme_kr = {
        1: "인더스트리얼",
        2: "유러피안",
        3: "클래식",
        4: "에스닉",
        5: "컨트리",
        6: "캐주얼",
        7: "로맨틱",
        8: "모던",
        9: "미니멀",
        10: "친환경",
        11: "에클레틱",
        12: "빈티지",
        # default
        13: "카페"
    }

cafe_theme_en = {
        1: "industrial",
        2: "european",
        3: "classic",
        4: "ethnic",
        5: "country",
        6: "casual",
        7: "romantic",
        8: "modern",
        9: "minimal",
        10: "environmental",
        11: "eclectic",
        12: "vintage",
        # default
        13: "default"
    }

from datetime import datetime
today = datetime.now().day
index = today % 13
if index == 0:
    index = 13

print("금일 카페 테마 -> " + cafe_theme_kr[index])

# input keyword
search_keyword = cafe_theme_kr[index] + " 카페"
if index == 13:
    search_keyword = "카페"

# save directory
save_directory_name = cafe_theme_en[index]

# string formatting
url = f"https://www.bing.com/images/search?q={quote_plus(search_keyword)}&form=HDRSC2&first=1&scenario=ImageBasicHover"

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
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

current_img_count = len(os.walk("C:/cafe-img/" + save_directory_name + "/").__next__()[2])
print(current_img_count)

# only crawling src attributes
for i in img:
    try:
        imgurl.append(i.attrs["src"])
    except KeyError:
        imgurl.append(i.attrs["data-src"])

n = 1
for i in imgurl:
    urlretrieve(i, "C:/cafe-img/" + save_directory_name + "/" + str(current_img_count + n) + ".jpg")
    n += 1

# termination
driver.close()

