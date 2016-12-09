from PIL import Image
from io import BytesIO
import requests


def download(url):
    try:
        r = requests.get(url, timeout=1)
        im = Image.open(BytesIO(r.content))
        name = increment_name('bing.jpg')
        im.save(name + '.jpg')
    except requests.exceptions.Timeout:
        print('Timeout: %s' % url)


def increment_name(base, directory=None):
    i = 0
    existing = os.listdir(directory)
    while True:
        trial_name = base.split('.')[0] + str(i) + '.' + base.split('.')[1]
        if trial_name not in existing:
            return trial_name
        else:
            i += 1

if __name__ == '__main__':
    f = open('BMW_M5_Sedan_2010.txt', 'r')
    for line in f:
        try:
            download(line)
        except Exception as e:
            print(e)