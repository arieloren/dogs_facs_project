import os
import shutil
import glob

def drop_redundant_txt(work_path,garbage_path):
    images_dict={}
    for subdir, dirs, files in os.walk(work_path):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                images_dict[filename]=""

    for subdir, dirs, files in os.walk(work_path):
        for filename in files:
            if filename.endswith(".txt"):
                #jpg
                key=filename[:-4]+".jpg"
                if key in images_dict:
                    images_dict[key]=filename
                else: #jpeg
                    key = filename[:-4] + ".jpeg"
                    if key in images_dict:
                        images_dict[key] = filename
                    else:
                        shutil.move(subdir+"/"+filename, garbage_path)

if __name__ == '__main__':
    work_path='D:/Amir/Machine_Learning_Course_Primrose/Final_Project/dog_faces_dataset_many_datasets/example'
    garbage_path = 'D:/Amir/Machine_Learning_Course_Primrose/Final_Project/dog_faces_dataset_many_datasets/garbage'
    drop_redundant_txt(work_path,garbage_path)