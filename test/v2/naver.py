from urllib.request import urlopen
from selenium import webdriver
import sys
import io
import custom

def do_naver_crawling():

    crawling_util = custom.util.CrawlingUtil()

    # for printing korean
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

    # crawling img files referring to cafe themes
    cafe_theme_kr = crawling_util.get_category_list_kr()
    cafe_theme_en = crawling_util.get_category_list_en()

    # index
    index = crawling_util.get_index()
    today_theme = cafe_theme_kr[index]

    # search keyword
    search_keyword = crawling_util.get_search_keyword(today_theme, index)
    save_directory_name = cafe_theme_en[index]

    url = crawling_util.get_url(custom.type.SiteType.NAVER.value, search_keyword)
    driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
    driver.implicitly_wait(3)
    driver.get(url)

    for i in range(500):
        driver.execute_script("window.scrollBy(0,10000)")

    img_urls = driver.find_elements_by_tag_name("span.img_border")

    total_count = crawling_util.get_file_cnt(save_directory_name)

    n = total_count + 1
    for index, img in enumerate(img_urls[0:]):
        img.click()
        html_objects = driver.find_element_by_tag_name('img._image_source')
        current_src = html_objects.get_attribute('src')

        t = urlopen(current_src).read()
        if index < 600:
            File = open(crawling_util.get_save_path(save_directory_name) + str(n) + '.jpg', 'wb')
            File.write(t)
            n += 1
        else:
            driver.close()
            break