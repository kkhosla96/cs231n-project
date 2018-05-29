import numpy as np
import os
from matplotlib import pyplot as plt
import matplotlib
import time

from PIL import Image

image_directory = "./train2017"

sub_folders = [dI for dI in os.listdir(image_directory) if os.path.isdir(os.path.join(image_directory, dI))]
print(sub_folders)

count = 0
for sub in sub_folders:
    sub_directory = os.path.join(image_directory, sub)
    for image_name in os.listdir(sub_directory):
        image_location = os.path.join(sub_directory, image_name)
        im = Image.open(image_location)
        arr = np.asarray(im)
        actual_name = image_name.split(".")[0]
        os.remove(image_location)
        np.save(os.path.join(image_directory, actual_name + ".npy"), arr)
        count += 1


