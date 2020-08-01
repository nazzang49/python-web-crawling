import os
from _datetime import datetime
from urllib.parse import quote_plus

# common source or logic for crawling at multiple browser
class CrawlingUtil:

    def get_category_list_kr(self):
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
            13: "카페"
        }
        return cafe_theme_kr

    def get_category_list_en(self):
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
            13: "cafe"
        }
        return cafe_theme_en

    def get_file_cnt(self, save_directory_name):
        return len(os.walk("C:/cafe-img/" + save_directory_name + "/").__next__()[2])

    def get_index(self):
        today = datetime.now().day
        index = today % 13
        if index == 0:
            index = 13
        return index

    def get_search_keyword(self, today_theme, index):
        if index == 13:
            today_theme = "카페"
        return today_theme + " 카페"

    def get_url(self, site_name, search_keyword):
        if site_name == "chrome":
            return f"https://www.google.com/search?q={quote_plus(search_keyword)}&sxsrf=ALeKk01n9CbhJFSTR5dLoacGQlXGMfTBTg:1593337667405&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjY0rCtnaTqAhWUQN4KHcV3B5oQ_AUoAnoECA4QBA&biw=1920&bih=987"
        elif site_name == "naver":
            return f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={quote_plus(search_keyword)}"
        elif site_name == "bing":
            return f"https://www.bing.com/images/search?q={quote_plus(search_keyword)}&form=HDRSC2&first=1&scenario=ImageBasicHover"
        elif site_name == "unsplash":
            return f"https://unsplash.com/s/photos/{quote_plus(search_keyword)}"

    def get_save_path(self, save_directory_name):
        return "C:/cafe-img/" + save_directory_name + "/"