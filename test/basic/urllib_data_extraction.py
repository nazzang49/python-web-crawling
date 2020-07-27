# urllib
import urllib.request as dw

# test url
img_url = "https://images.mypetlife.co.kr/content/uploads/2019/09/06150205/cat-baby-4208578_1920.jpg"
html_url = "http://google.com"

save_path_1 = "d:/test-cat.png"
save_path_2 = "d:/test-index.html"

# download document
dw.urlretrieve(img_url, save_path_1)
dw.urlretrieve(html_url, save_path_2)

print("download-done")