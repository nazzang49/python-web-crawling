# crawling of bing img
# keyword is 카페
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from selenium import webdriver
import sys
import io

util = __import__("%s" %("util"), fromlist=["util"])
crawling_util = getattr(util, "CrawlingUtil")

type = __import__("%s" %("type"), fromlist=["type"])

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

# cafe themes
cafe_theme_kr = crawling_util.get_category_list_kr(0)
cafe_theme_en = crawling_util.get_category_list_en(0)

# index
index = crawling_util.get_index(0)
today_theme = cafe_theme_kr[index]

# search keyword
search_keyword = crawling_util.get_search_keyword(0, today_theme, index)
save_directory_name = cafe_theme_en[index]

url = crawling_util.get_url(0, type.SiteType.BING.value, search_keyword)
driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(3)
driver.get(url)
html = driver.page_source
bs = BeautifulSoup(html, "html.parser")

for i in range(500):
    driver.execute_script("window.scrollBy(0, 10000)")

# find all img tags
img = bs.find_all("img", class_="mimg")
img_urls = []
total_count = crawling_util.get_file_cnt(0, save_directory_name)

for i in img:
    try:
        img_urls.append(i.attrs["src"])
    except KeyError:
        img_urls.append(i.attrs["data-src"])

n = total_count + 1
for i in img_urls:
    urlretrieve(i, crawling_util.get_save_path(0, save_directory_name) + str(n) + ".jpg")
    n += 1

driver.close()

