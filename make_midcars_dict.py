import os
import numpy as np


def make_midcars_dict():
    dog_values = []
    for f in os.listdir('/home/rgio/FGIC/dogs/dog_photos'):
        dog_values.append(len(os.listdir('/home/rgio/FGIC/dogs/dog_photos/%s' % f)))
    print(dog_values)

    print(np.mean(dog_values))
    print(np.std(dog_values))

if __name__ == '__main__':
    make_midcars_dict()
