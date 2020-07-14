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
url = f"https://www.google.com/search?q={quote_plus(search_keyword)}&sxsrf=ALeKk01n9CbhJFSTR5dLoacGQlXGMfTBTg:1593337667405&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjY0rCtnaTqAhWUQN4KHcV3B5oQ_AUoAnoECA4QBA&biw=1920&bih=987"

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
# waiting for 3sec
driver.implicitly_wait(3)
driver.get(url)

for _ in range(10000):
    driver.execute_script("window.scrollBy(0,30000)")

photo_list = []

photo_list = driver.find_elements_by_tag_name("img.rg_i.Q4LuWd")

# check current download img amounts -> preventing from overwritten
current_img_count = len(os.walk("C:/cafe-crawling-chrome/").__next__()[2])
print(current_img_count)

count = current_img_count + 1

for index, img in enumerate(photo_list[0:]):
    # click default img
    webdriver.ActionChains(driver).move_to_element(img).click(img).perform()
    html_objects = driver.find_element_by_tag_name('img.n3VNCb')
    current_src = html_objects.get_attribute('src')

    t = urlopen(current_src).read()
    if index < 600:
        filename = search_keyword + str(count) + ".jpg"
        File = open('C:/cafe-crawling-chrome/' + search_keyword + str(count) + '.jpg', 'wb')
        File.write(t)
        count += 1
        print("img-save" + str(count))
    else:
        driver.close()
        break
