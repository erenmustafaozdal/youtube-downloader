import os
import pytube

url = input("Video adresi yazın: ")
path = "./downloads"

# eğer klasör yoksa oluştur
if not os.path.exists(path):
    os.mkdir(path)

pytube.YouTube(url).streams.get_highest_resolution().download(path)
