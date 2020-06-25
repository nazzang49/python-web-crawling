# urllib
import urllib.request as dw

# test url
img_url = "https://images.mypetlife.co.kr/content/uploads/2019/09/06150205/cat-baby-4208578_1920.jpg"
html_url = "http://google.com"

save_path_1 = "d:/test-cat.png"
save_path_2 = "d:/test-index.html"

# read data from WEB
f = dw.urlopen(img_url).read()

# mode type
# w = write
# r = read
# a = add
# b = suffix
save_file_1 = open(save_path_1, 'wb')

# write data to local PC
save_file_1.write(f)
save_file_1.close()

# with statement -> reducing lines
with open(save_path_1, 'wb') as save_file_1:
    save_file_1.write(f)

print("download-done")