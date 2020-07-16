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
current_img_count = len(os.walk("C:/cafe-img/" + save_directory_name + "/").__next__()[2])
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
        File = open('C:/cafe-img/' + save_directory_name + "/" + str(count) + '.jpg', 'wb')
        File.write(t)
        count += 1
        print("img-save" + str(count))
    else:
        driver.close()
        break
