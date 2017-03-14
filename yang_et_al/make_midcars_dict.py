import os
import numpy as np
import pickle
from random import gauss


def make_midcars_dict():
    dog_values = []
    for f in os.listdir('/home/rgio/FGIC/dogs/dog_photos'):
        dog_values.append(len(os.listdir('/home/rgio/FGIC/dogs/dog_photos/%s' % f)))

    mu = np.mean(dog_values)
    sigma = np.std(dog_values)

    midcars_dict = {}
    for f in os.listdir('/home/rgio/FGIC/midcars/car_photos'):
        midcars_dict[f] = int(gauss(mu, sigma))

    with open('midcars_dict.pkl', 'wb') as f:
        pickle.dump(midcars_dict, f)
        f.close()


if __name__ == '__main__':
    make_midcars_dict()
