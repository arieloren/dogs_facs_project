# Libraries
import re
import os
import shutil


def dog_type_selection(orig_path, dest_path, dogs_names):  # dogs_name must be a list with strings part inside it
    for dog in dogs_names:

        for subdir, dirs, files in os.walk(orig_path):
            for filename in files:
                filepath = subdir + os.sep + filename
                if (re.findall(dog, filename)):  # check if the dogs name match the filename
                    shutil.move(filepath, dest_path)


if __name__ == '__main__':
    orig_path = 'C:/Users/user/Documents/Ariel/DL_lab_project/oxford_dog_dataset/images'
    dest_path = 'C:/Users/user/Documents/Ariel/DL_lab_project/oxford_dog_dataset/unwanted_dogs'
    unwanted_list = ['Abyssinian', 'basset_hound']
    dog_type_selection(orig_path, dest_path, unwanted_list)
