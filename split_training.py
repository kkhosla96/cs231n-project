import os

train_folder = "./train2017"

filenames = os.listdir(train_folder)

per_subfolder = 1000
chunks = [filenames[x:x+per_subfolder] for x in range(0, len(filenames), per_subfolder)]

for subfolder_number in range(len(chunks)):
    subfolder_name = "set_" + str(subfolder_number)
    subfolder_path = os.path.join(train_folder, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    filenames_in_this_set = chunks[subfolder_number]
    for filename in filenames_in_this_set:
        image_path = os.path.join(train_folder, filename)
        os.rename(image_path, os.path.join(subfolder_path, filename))