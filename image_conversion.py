from PIL import Image
import os

def process(image_path):
    im = Image.open(image_path).convert('RGB')
    if im.format != 'JPEG':
        if len(image_path.split('.')) > 2:
            raise ValueError('Bad filename split')
        name = image_path.split('.')[0]
        os.remove(image_path)
        im.save(name + '.jpg')

total = len(os.listdir('car_photos'))
i = 0
for td in os.listdir('car_photos'):
    i += 1
    for ip in os.listdir('car_photos/' + td):
        try:
            process('car_photos/%s/%s' % (td, ip))
        except Exception:
            os.remove('car_photos/%s/%s' % (td, ip))
    print('\rProgress: %d of %d' % (i, total), end='')
