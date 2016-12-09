import urllib
import os


def download(url, dest):
    try:
        urllib.request.urlretrieve(url, dest)
    except Exception as e:
        print(e)


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
    for text_file_name in os.listdir('/home/rgio/FGIC/midcars/image_urls/'):
        text_file = open(text_file_name, 'r')
        dest_directory = text_file_name.replace('.txt', '')
        for line in text_file:
            dest_file_name = increment_name('bing.jpg')
            dest = '/home/rgio/FGIC/midcars/car_photos/%s/%s' % (dest_directory, dest_file_name)
            download(line, dest)
