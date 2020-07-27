import enum

# name - value
class SiteType(enum.Enum):
    CHROME = "chrome"
    NAVER = "naver"
    BING = "bing"
    UNSPLASH = "unsplash"

class LangType(enum.Enum):
    KR = "kr"
    EN = "en"