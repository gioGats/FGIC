# Fine Grained Image Classification (FGIC)
This project is an update to the 2015 work of Xie, Yang, Wang, and Lin available [online here](http://vcl.ucsd.edu/~sxie/pdf/hyper-cvpr2015.pdf). 

Specifically it attempts to equal or best the performance of their methods using transfer learning and Google Inception Image Classifier as [described here](https://research.googleblog.com/2016/03/train-your-own-image-classifier-with.html).
Basic code requires TensorFlow v0.12 release.  More recent releases are not compatible.  See file structure section for proper environment setup.

## Current Best Performance:
Stanford Dogs: 
Stanford Cars:

## Methodology:
### Raw
- Train on only the data available in the Stanford Dogs/Cars datasets.
- This is approximately 80 images per class for dogs and 30 images per class for cars.
### Mid Range Boosting - Cars Only
- Uses mean and standard deviation of the number of images per class in the dogs dataset to create a normal distribution
- Samples from this distribution for the number of images per class in the cars dataset and saves this to a dumped dictionary.
- Uses Bing Image API to collect images with the class name as query
- 'midcars'
 
## Requirements
- TensorFlow v0.12
- py_bing_search

## File Structure from ~/
/FGIC
    /FGIC - git clone of this repository
        /cars_run.sh - run to train on the cars dataset
        /dogs_run.sh - run to train on the dogs dataset
        /midcars_run.sh - run to train on the midcars dataset
        /ImageCollector.py - class and main method for collecting images for midcars dataset. Currently not functioning.
        /make_midcars_dict.py - implements sampling and dictionary creation described in Mid Range Boosting
    /cars
        /car_photos - sub-directories are named by class and contain example images of that class
    /dogs
        /dog_photos - sub-directories are named by class and contain example images of that class
    /midcars
        /car_photos - sub-directories are named by class and contain example images of that class
        /image_urls - text files of image results to download for testing and debugging
    /stanford_dogs_data - unprocessed data backup folder, request .tar.gz
    /stanford_cars_data - unprocessed data backup folder, request .tar.gz
/tensorflow - git clone of v0.12 release
