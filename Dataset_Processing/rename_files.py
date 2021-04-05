import os, glob

def rename_files_in_dir(orig_path):
    for subdir, dirs, files in os.walk(orig_path):
        for filename in files:
            print(str(filename))
            origin = subdir+"/"+filename

            if filename.endswith(".jpg.txt"):
                print("before: " + str(origin))
                destination = origin[:-8]+".txt"
                os.rename(origin, destination)
                print("after: " + str(destination))
            elif filename.endswith(".jpeg.txt"):
                print("before: " + str(origin))
                destination = origin[:-9] + ".txt"
                os.rename(origin, destination)
                print("after: " + str(destination))

            if filename.endswith(").jpg"):
                print("before: " + str(origin))
                destination = origin[:-8] + ".jpg"
                os.rename(origin, destination)
                print("after: " + str(destination))
            elif filename.endswith(").jpeg"):
                print("before: " + str(origin))
                destination = origin[:-9] + ".jpeg"
                os.rename(origin, destination)
                print("after: " + str(destination))
    print("Finished!")


orig_path='D:/Amir/Machine_Learning_Course_Primrose/Final_Project/dog_faces_dataset_many_datasets/selected_data'
rename_files_in_dir(orig_path)

if __name__ == '__main__':
    for filepath in glob.iglob('D:/Amir/Machine_Learning_Course_Primrose/Final_Project/dog_faces_dataset_many_datasets/example/*.txt'):
        if (os.path.exists(filepath[:-4]+".jpg") or os.path.exists(filepath[:-5]+".jpeg")):
            pass
        else:
            print(str(filepath))
            os.remove(filepath)