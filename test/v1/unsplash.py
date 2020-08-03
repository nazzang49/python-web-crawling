from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from selenium import webdriver
import sys
import io
import custom
import time

def do_unsplash_crawling():

    crawling_util = custom.CrawlingUtil()

    # for printing korean
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

    # cafe themes
    cafe_theme_kr = crawling_util.get_category_list_kr()
    cafe_theme_en = crawling_util.get_category_list_en()

    index = crawling_util.get_index()
    today_theme = cafe_theme_en[index]

    # search_keyword = crawling_util.get_search_keyword(today_theme, index)
    search_keyword = "cafe"
    save_directory_name = cafe_theme_en[index]

    url = crawling_util.get_url(custom.SiteType.UNSPLASH.value, search_keyword)
    driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
    driver.implicitly_wait(3)
    driver.get(url)
    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    for i in range(500):
        driver.execute_script("window.scrollBy(0, 1000)")
        time.sleep(1)

    total_count = crawling_util.get_file_cnt(save_directory_name)

    img = bs.select("._2zEKz")
    img_urls = []

    # only crawling src attributes
    for i in img:
        if i.get("src"):
            img_urls.append(i.get("src"))

    n = total_count + 1
    # save as other name
    for i in img_urls:
        urlretrieve(i, crawling_util.get_save_path(save_directory_name) + str(n) + ".jpg")
        n += 1

    # termination
    driver.close()