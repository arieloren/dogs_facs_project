# Libraries
import re
import shutil
import os


def dogs_type_selection(orig_path, dest_path, dogs_names):  # dogs_name must be a list with strings parts inside it

    if len(dogs_names) != 0:

        for dog in dogs_names:

            for subdir, dirs, files in os.walk(orig_path):
                for filename in files:
                    filepath = subdir + os.sep + filename
                    if (re.findall(dog, filename)):  # check if the dogs name match the filename
                        shutil.move(filepath, dest_path)

    else:
        print("the dogs list is empty")

def remove_unwanted_dog_files(orig_path, dest_path,unwanted_breeds, unwanted_suffixes):
    if len(unwanted_breeds) != 0 or len(unwanted_suffixes) != 0:
        #suffixes:
        for suffix in unwanted_suffixes:
            for subdir, dirs, files in os.walk(orig_path):
                for filename in files:
                    filepath = subdir + os.sep + filename
                    if filename.endswith("."+suffix):
                        shutil.move(filepath, dest_path)
        #breeds:
        for dog in unwanted_breeds:
            for subdir, dirs, files in os.walk(orig_path):
                for filename in files:
                    filepath = subdir + os.sep + filename
                    if (re.findall(dog, filename)):  # check if the dogs name match the filename
                        shutil.move(filepath, dest_path)


if __name__ == '__main__':
    orig_path = 'D:/Amir/Machine_Learning_Course_Primrose/Final_Project/preprocessed_dataset'
    dest_path = 'D:/Amir/Machine_Learning_Course_Primrose/Final_Project/unwanted_dogs'
    unwanted_breeds = ["american_bulldog","american_pit_bull_terrier","chihuahua","havanese","japanese_chin","keshond","miniature_pinscher","pomeranian","pug","samoyed","scotish_terrier", "shiba_inu","staffordshire_bull_terrier", "wheaten_terrier","yorkshire_terrier"]
    unwanted_suffixes=["xml"]
    remove_unwanted_dog_files(orig_path, dest_path, unwanted_breeds, unwanted_suffixes)