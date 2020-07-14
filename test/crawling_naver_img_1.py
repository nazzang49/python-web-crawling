# crawling of google img
# keyword is 카페
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlretrieve, urlopen
from selenium import webdriver
import sys
import io
import os

# for printing korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

# input keyword
search_keyword = "카페"
# string formatting
url = f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={quote_plus(search_keyword)}"

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
# waiting for 3sec
driver.implicitly_wait(3)
driver.get(url)

for _ in range(10000):
    driver.execute_script("window.scrollBy(0,30000)")

photo_list = []

photo_list = driver.find_elements_by_tag_name("span.img_border")

current_img_count = len(os.walk("C:/cafe-crawling-naver/").__next__()[2])
print(current_img_count)

count = current_img_count + 1

for index, img in enumerate(photo_list[0:]):
    # click default img
    img.click()
    html_objects = driver.find_element_by_tag_name('img._image_source')
    current_src = html_objects.get_attribute('src')

    t = urlopen(current_src).read()
    if index < 700:
        filename = search_keyword + str(count) + ".jpg"
        File = open('C:/cafe-crawling-naver/' + search_keyword + str(count) + '.jpg', 'wb')
        File.write(t)
        count += 1
        print("img-save" + str(count))
    else:
        driver.close()
        break
