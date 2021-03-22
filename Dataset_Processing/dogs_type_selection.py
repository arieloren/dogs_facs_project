# Libraries
import re
import shutil


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


if __name__ == '__main__':
    orig_path = 'C:/Users/user/Documents/Ariel/DL_lab_project/oxford_dog_dataset/images'
    dest_path = 'C:/Users/user/Documents/Ariel/DL_lab_project/oxford_dog_dataset/unwanted_dogs'
    unwanted_list = []
    dogs_type_selection(orig_path, dest_path, unwanted_list)
