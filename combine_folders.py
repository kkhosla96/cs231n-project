import os

image_dir = "./images"
current_image_dir = "./tiny-imagenet-200"

new_train = image_dir + "/train"
new_val = image_dir + "/val"
new_test = image_dir + "/test"

if not os.path.exists(image_dir):
    os.makedirs(image_dir)
    os.makedirs(new_train)
    os.makedirs(new_val)
    os.makedirs(new_test)
    
    
# copy all the files to the right directory
current_train = current_image_dir + "/train"
current_val = current_image_dir + "/val" + "/images"
current_test = current_image_dir + "/test" + "/images"

for folder_name in os.listdir(current_train):
    these_images_dir = os.path.join(current_train, folder_name) + "/images"
    for image_name in os.listdir(these_images_dir):
        os.rename(os.path.join(these_images_dir, image_name), os.path.join(new_train, image_name))
        # print(these_images_dir + image_name)
        
for image_name in os.listdir(current_val):
    os.rename(os.path.join(current_val, image_name), os.path.join(new_val, image_name))

for image_name in os.listdir(current_test):
    os.rename(os.path.join(current_test, image_name), os.path.join(new_test, image_name))

