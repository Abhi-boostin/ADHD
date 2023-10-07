import os
import requests
from PIL import Image
from io import BytesIO
import ctypes
from datetime import datetime
time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
url = '/photos/random'
api ='tZ3SekTOTwynvuBna9GiAI9LL-Ku0W77seHBAxGR-ps'
r = requests.get(f'https://api.unsplash.com/photos/random?client_id=tZ3SekTOTwynvuBna9GiAI9LL-Ku0W77seHBAxGR-ps').json()
def fetch():
    imageurl = r['urls']['regular']
    return imageurl
def set():
    img = Image.open(BytesIO(requests.get(fetch()).content)) 
    img_path ='C:\\Users\\Administrator\\Desktop\\ADHD'
    try:
     os.mkdir(img_path)
    except OSError as error:
     pass
    img.save(f'{img_path}\\{str(time)}wallpaper.jpg')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{img_path}\\{str(time)}wallpaper.jpg', 3)


def main():
    set()
if __name__ == '__main__':
    main()