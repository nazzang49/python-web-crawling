# download naver banner
    # image
    # video
import urllib.request as request
# from + package name / import + util name (=class)
from urllib.parse import urlencode

image_url = "https://ssl.pstatic.net/tveta/libs/1292/1292442/2c85b27803114fdfd4cc_20200624175504314_1.jpg"
video_url = "https://youtu.be/DdYQNF_PBD8"

req = request.urlopen(image_url)
# before read -> can check request info
# print(req.geturl())
# print(req.getheaders())
# print(req.status)
# print(req.info())

# read
req = request.urlopen(image_url).read()

print(req)
# save
with open("d:/naver_banner_img.jpg", 'wb') as save_file_1:
    save_file_1.write(req)

# read
req = request.urlopen(video_url).read()
print(req)

# save
with open("d:/youtube-vid.html", 'wb') as save_file_1:
    save_file_1.write(req)

