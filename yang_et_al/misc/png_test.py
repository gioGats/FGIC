import os
import imghdr

for f in os.listdir('sheepdog'):
    stream = open('sheepdog/' + f, 'rb')
    print('%s: %s'% (f, imghdr.what(stream)))
    stream.close()
