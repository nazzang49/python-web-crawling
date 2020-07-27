# download youtube and convert it to mp3

import os
import pytube
import subprocess

# print current directory
# D:\python-web-crawling\test
print(os.getcwd())

# change os.path directory
os.chdir("d:/")

# make directory
if not os.path.exists("youtube-download"):
    os.mkdir("youtube-download")

yt = pytube.YouTube("https://www.youtube.com/watch?v=scfA6ERKe_k")
vid = yt.streams.all()
print(vid)

# download through specific stream type that i want
for i in range(len(vid)):
    print(i, " : ", vid[i])

# input stream type
    # v1 -> string
stream_type = int(input("which type of steam do you want : "))

# save youtube video by first stream type
save_path = "d:/youtube-download"
vid[0].download(save_path)

converted_file_name = input("what name do you want this file to be converted : ")
origin_file_name = vid[stream_type].default_filename

# (in basic) should enroll ffmpeg to system env field
subprocess.call(['ffmpeg', '-i',
                 os.path.join(save_path, origin_file_name),
                 os.path.join(save_path, converted_file_name)])