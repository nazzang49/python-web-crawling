# urllib package
import urllib.request as req
# from + package name / import + custom name (=class)
from urllib.parse import urlparse

# test url
url = "https://www.naver.com/"
# request object
mem = req.urlopen(url)

# <http.client.HTTPResponse object at 0x000002B1361920C8>
print(mem)
# https://www.naver.com/
print(mem.geturl())
# Server: NWS
# Content-Type: text/html; charset=UTF-8
# Cache-Control: no-cache, no-store, must-revalidate
# Pragma: no-cache
# P3P: CP="CAO DSP CURa ADMa TAIa PSAa OUR LAW STP PHY ONL UNI PUR FIN COM NAV INT DEM STA PRE"
# X-Frame-Options: DENY
# X-XSS-Protection: 1; mode=block
# Strict-Transport-Security: max-age=63072000; includeSubdomains
# Referrer-Policy: unsafe-url
# Date: Sat, 27 Jun 2020 06:32:46 GMT
# Transfer-Encoding: chunked
# Connection: close
# Connection: Transfer-Encoding
# Set-Cookie: PM_CK_loc=5a30430feef427fb932ebc7ad0b40e97e3b60f7f465168657210cd56ee2e8fda; Expires=Sun, 28 Jun 2020 06:32:46 GMT; Path=/; HttpOnly
print(mem.info())

# status code
    # 200 -> success
    # 404 -> not found
    # 500 -> internal server error
    # 403 -> authorization rejected
print(mem.status)
# print(mem.getcode())

# [('Server', 'NWS'), ('Content-Type', 'text/html; charset=UTF-8'), ('Cache-Control', 'no-cache, no-store, must-revalidate'), ('Pragma', 'no-cache'), ('P3P', 'CP="CAO DSP CURa ADMa TAIa PSAa OUR LAW STP PHY ONL UNI PUR FIN COM NAV INT DEM STA PRE"'), ('X-Frame-Options', 'DENY'), ('X-XSS-Protection', '1; mode=block'), ('Strict-Transport-Security', 'max-age=63072000; includeSubdomains'), ('Referrer-Policy', 'unsafe-url'), ('Date', 'Sat, 27 Jun 2020 06:44:26 GMT'), ('Transfer-Encoding', 'chunked'), ('Connection', 'close'), ('Connection', 'Transfer-Encoding'), ('Set-Cookie', 'PM_CK_loc=5a30430feef427fb932ebc7ad0b40e97e3b60f7f465168657210cd56ee2e8fda; Expires=Sun, 28 Jun 2020 06:44:26 GMT; Path=/; HttpOnly')]
print(mem.getheaders())

# python key type
    # dict {}
    # list []
    # tuple ()

# core function -> can check naver main page by a list of html tags
print(mem.read().decode("utf-8"))

# ParseResult(scheme='https', netloc='www.naver.com', path='', params='', query='test=test', fragment='')
    # query = queryString
print(urlparse("https://www.naver.com?test=test"))

