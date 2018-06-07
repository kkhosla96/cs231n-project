import os
import random

train_folder = "./train2017"
val_folder = "./val2017"

filenames = os.listdir(train_folder)

num_validation = 2000

validation_names = random.sample(filenames, num_validation)

for name in validation_names:
    old_name = os.path.join(train_folder, name)
    new_name = os.path.join(val_folder, name)
    os.rename(old_name, new_name)


