# basic of web parsing
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlopen
import sys
import io

# for printing korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

# get naver main page html tags
html = urlopen("https://www.naver.com/").read().decode("utf-8")
# print(html)

bs = BeautifulSoup(html, "html.parser")

a_tags = bs.findAll("a")
# print(a_tags)
# print(a_tags[0])

# get text value of this a-tag
# print(a_tags[0].getText())

a_tags_text = []
for tag in a_tags:
    # if value is exist -> append
    # if a_tags[i].getText():
    a_tags_text.append(tag.getText())

print(len(a_tags_text))
print(a_tags_text)

# get all a-tags which class name is dsc
a_tags = bs.findAll("a", {"class": "dsc"})
print(a_tags)
