# urllib package
import urllib.request as req
# from + package name / import + util name (=class)
from urllib.parse import urlencode

# https://www.ipify.org/
api = "https://api.ipify.org"

values = {
    'format': 'json'
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