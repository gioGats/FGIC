from py_bing_search import PyBingImageSearch
from urllib.request import urlretrieve
from PIL import Image
import os
import pickle
import time


class ImageCollector(object):
    def __init__(self, target_directory=None):
        self.target = target_directory
        if target_directory is not None:
            os.chdir(target_directory)

    def convert(self, image_path):
        im = Image.open(image_path).convert('RGB')
        if im.format != 'JPEG':
            if len(image_path.split('.')) > 2:
                raise ValueError('Bad filename split')
            name = image_path.split('.')[0]
            os.remove(image_path)
            im.save(name + '.jpg')

    def convert_all(self, directory=None):
        for im in os.listdir(directory):
            try:
                self.convert(im)
            except Exception:
                os.remove(im)

    def get_image_urls(self, keyword, number, existing_urls=False):
        if not existing_urls:
            API_KEY = '40E5RsqfihlGEm1ehQpKVfoBLntynFWkH7Uv+On0UM8'
            bing_image = PyBingImageSearch(API_KEY, keyword)
            # image_filters is optional
            results = bing_image.search(limit=number, format='json')  # 1-50
            urls = []
            for i in results:
                urls.append(i.media_url)
            return urls
        else:
            raise NotImplementedError

    def download_url(self, url, dest):
        # ISSUE
        try:
            urlretrieve(url, dest)
        except Exception as e:
            print(e)

    def increment_name(self, base, directory=None):
        i = 0
        existing = os.listdir(directory)
        while True:
            trial_name = base.split('.')[0] + str(i) + '.' + base.split('.')[1]
            if trial_name not in existing:
                return trial_name
            else:
                i += 1


class MidCarImageCollector(ImageCollector):
    def __init__(self, target_directory='/home/rgio/FGIC/midcars/car_photos', existing_urls=False):
        with open('midcars_dict.pkl', 'rb') as f:
            self.target_sizes = pickle.load(f)
            f.close()
        super().__init__(target_directory)
        if existing_urls:
            raise NotImplementedError

    def download(self):
        total_dirs = len(os.listdir('/home/rgio/FGIC/midcars/car_photos'))
        current_dir = 0
        for f in os.listdir('/home/rgio/FGIC/midcars/car_photos'):
            current_number = len(os.listdir('/home/rgio/FGIC/midcars/car_photos/%s' % f))
            desired_number = self.target_sizes[f]
            print('\rDirectory %.3d of %.3d | Image %.3d of %.3d' %
                  (current_dir, total_dirs, current_number, desired_number), end='')
            while current_number < desired_number:
                for t in self.get_image_urls(f.replace('_', ' '), 2 * (desired_number - current_number)):
                    self.download_url(t, self.increment_name('bing.jpg'))  # ISSUE
                self.convert_all('/home/rgio/FGIC/midcars/car_photos/%s' % f)
                current_number = len(os.listdir('/home/rgio/FGIC/midcars/car_photos/%s' % f))
                print('\rDirectory %.3d of %.3d | Image %.3d of %.3d' %
                      (current_dir, total_dirs, current_number, desired_number), end='')
                time.sleep(1)
            current_dir += 1
        print()

    def url_dump(self):
        total_dirs = len(os.listdir('/home/rgio/FGIC/midcars/car_photos'))
        current_dir = 0
        for f in os.listdir('/home/rgio/FGIC/midcars/car_photos'):
            current_number = len(os.listdir('/home/rgio/FGIC/midcars/car_photos/%s' % f))
            desired_number = self.target_sizes[f]
            print('\rDirectory %.3d of %.3d | Image %.3d of %.3d' %
                  (current_dir, total_dirs, current_number, desired_number), end='')
            if current_number < desired_number:
                dump_file = open('/home/rgio/FGIC/midcars/image_urls/%s.txt' % f, 'w')
                for t in self.get_image_urls(f.replace('_', ' '), 2 * (desired_number - current_number)):
                    try:
                        dump_file.write('%s\n' % t)
                    except UnicodeEncodeError:
                        pass
                dump_file.close()
            time.sleep(0.5)
            current_dir += 1


def initial_testing():
    ic = ImageCollector()
    print(ic.increment_name('cars_run.sh'))
    urls = ic.get_image_urls('cats', 10)
    print(urls)
    for u in urls:
        name = ic.increment_name('cat.jpg')
        ic.download_url(u, name)


if __name__ == '__main__':
    ic = MidCarImageCollector()
    ic.download() # ISSUE Getting 403 errors
    #ic.url_dump()