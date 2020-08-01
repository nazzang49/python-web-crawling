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
url = f"https://www.bing.com/images/search?q={quote_plus(search_keyword)}&form=HDRSC2&first=1&scenario=ImageBasicHover"

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
# waiting for 3sec
driver.implicitly_wait(3)
driver.get(url)

for _ in range(10000):
    driver.execute_script("window.scrollBy(0,30000)")

photo_list = []

photo_list = driver.find_elements_by_tag_name("img.mimg")

current_img_count = len(os.walk("C:/cafe-crawling-bing/").__next__()[2])
print(current_img_count)

count = current_img_count + 1

for index, img in enumerate(photo_list[0:]):
    # click v1 img
    webdriver.ActionChains(driver).move_to_element(img).click(img).perform()
    html_objects = driver.find_element_by_tag_name('img.nofocus')
    current_src = html_objects.get_attribute('src')

    t = urlopen(current_src).read()
    if index < 700:
        filename = search_keyword + str(count) + ".jpg"
        File = open('C:/cafe-crawling-bing/' + search_keyword + str(count) + '.jpg', 'wb')
        File.write(t)
        count += 1
        print("img-save" + str(count))
    else:
        driver.close()
        break
