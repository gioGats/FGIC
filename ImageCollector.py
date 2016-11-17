from PIL import Image
import os


class ImageCollector(object):
    def __init__(self, target_directory=None):
        self.target = target_directory
        os.chdir(target_directory)

    def convert(self, image_path):
        im = Image.open(image_path).convert('RGB')
        if im.format != 'JPEG':
            if len(image_path.split('.')) > 2:
                raise ValueError('Bad filename split')
            name = image_path.split('.')[0]
            os.remove(image_path)
            im.save(name + '.jpg')

    def convert_all(self):
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





def main():
    i = 0
    total = len(os.listdir('car_photos'))
    for d in os.listdir('car_photos'):
        if d == '.DS_Store':
            continue
        td = 'car_photos/' + d
        kw = d
        #print('Keyword: %s\nNum Images: %d\nProgress: %d of %d' % (kw,len(os.listdir(td)), i, total))
        print('Num Images: %d' % len(os.listdir(td)))
        i += 1
        if len(os.listdir(td)) < 0:
            image_search(kw)

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def image_search(keyword):
    query = keyword # you can change the query for the image  here
    image_type="ActiOn"
    query= query.split()
    query='+'.join(query)
    url="https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
    #print url
    #add the directory for your image here
    DIR="car_photos"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }
    soup = get_soup(url,header)


    ActualImages=[]# contains the link for Large original images, type of  image
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))

    #print  "there are total" , len(ActualImages),"images"

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    DIR = os.path.join(DIR, query.split()[0])

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    ###print images
    for i , (img , Type) in enumerate( ActualImages):
        try:
            req = urllib2.Request(img, headers={'User-Agent' : header})
            raw_img = urllib2.urlopen(req).read()

            cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
            #print cntr
            if len(Type)==0:
                f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
            else :
                f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')


            f.write(raw_img)
            f.close()
        except Exception as e:
            pass
            #print "could not load : "+img
            #print e

main()
