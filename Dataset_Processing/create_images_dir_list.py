import os


def create_list_directory_file(orig_path, dest_path):
    dest_file = open(dest_path, "w")
    for subdir, dirs, files in os.walk(orig_path):
        for filename in files:
            if filename[-4:] == ".jpg":
                img_path = dest_path + os.sep + filename
                dest_file.write(img_path)
                dest_file.write("\n")
    dest_file.close()

orig_path='D:\\Amir\\Machine_Learning_Course_Primrose\\Final_Project\\our_images'
dest_path='D:\\Amir\\Machine_Learning_Course_Primrose\\Final_Project\\our_images.txt'
create_list_directory_file(orig_path, dest_path)
# orig_path='/content/gdrive/MyDrive/facs_ariel_amir/our_images'
# dest_path='/content/darknet/data/our_images.txt'