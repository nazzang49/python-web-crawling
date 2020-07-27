# urllib package
import urllib.request as req
# from + package name / import + util name (=class)
from urllib.parse import urlencode

# https://www.ipify.org/
api = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

# https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001 -> rss address
values = {
    'ctxCd': '1001'
    # 'ctxCd': '1012' -> 보도자료_게시판
}
print('before', values)
params = urlencode(values)
# changed into queryString pattern
    # format=json
print('after', params)

url = api + "?" + params
print("request url", url)

req = req.urlopen(url).read().decode("utf-8")
# can check request-ip from server
    # {"ip":"210.108.244.205"}
print(req)