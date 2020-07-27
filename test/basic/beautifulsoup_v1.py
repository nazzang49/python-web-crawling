# basic of web parsing
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import io

# for printing korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

# automization of convert with urljoin
# hostname is fixed
    # http://test.com
base_url = "http://test.com/html/a.html"
# a.html -> b.html
print(">>", urljoin(base_url, "b.html"))
# a.html -> sub/b.html
print(">>", urljoin(base_url, "sub/b.html"))
# http://test.com/img/img.jpg
print(">>", urljoin(base_url, "../img/img.jpg"))

# using """ phrase -> emit new line sign \n
html = """
<html>
<body>
<div>
<h1>python-web-crawling-test</h1>
<h1>python-web-crawling-test-1</h1>
<p>this-is-p-tag</p>
</div>
</body>
</html>
"""
print(html)

# bs parsing object
    # html -> text component
bs = BeautifulSoup(html, "html.parser")
print(type(bs))
print(bs.prettify())

# get all tags of h1 in html -> list type
h1 = bs.findAll("h1")
# <h1>python-web-crawling-test</h1>
print(h1)
# python-web-crawling-test
    # core value that we need
print(h1[1].getText())
# <bound method Tag.get_text of <h1>python-web-crawling-test-1</h1>>
print(h1[1].get_text)