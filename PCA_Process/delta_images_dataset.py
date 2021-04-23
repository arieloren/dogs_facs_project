from PIL import Image
import numpy as np
import os


def resize_image(origin, h, w):  # resize image
    image = Image.open(origin)
    resized_image = image.resize((h, w))
    return resized_image


def create_mean_images_dataset(orig_folder_path, dest_folder_path, name_of_film, h, w):  # create delta images dataset
    frames_dataset = []
    for subdir, dirs, files in os.walk(orig_folder_path):
        for filename in files:
            if name_of_film == "all" or filename.find(name_of_film) != -1:
                # isfind=(filename.find(name_of_film))
                orig_path = subdir + os.sep + filename
                resized_image = resize_image(orig_path, h, w)
                frames_dataset.append(resized_image)

    if len(frames_dataset) > 0:
        N = len(frames_dataset)
        mean_frame = np.zeros((h, w, 3), np.float)
        for frame in frames_dataset:
            imarr = np.array(frame, dtype=np.float)
            mean_frame = mean_frame + imarr / N

        mean_frame = np.array(np.round(mean_frame), dtype=np.uint8)
        out = Image.fromarray(mean_frame, mode="RGB")
        dest_path = dest_folder_path + "/" + "mean_frame_of_" + name_of_film + ".jpg"
        out.save(dest_path)


def subtract_images(minuend_path, subtrahend_path, diff_path, h, w):
    minuend=resize_image(minuend_path, h, w)
    subtrahend =resize_image(subtrahend_path, h, w)

    minuend_buffer = np.asarray(minuend)
    subtrahend_buffer = np.asarray(subtrahend)

    diff_buffer = minuend_buffer - subtrahend_buffer

    delta_image = Image.fromarray(diff_buffer)
    delta_image.save(diff_path)


def create_delta_images(orig_folder_path, dest_folder_path, mean_frames_folder_path, name_of_film, h, w):
    mean_frame_path = mean_frames_folder_path + "/" + "mean_frame_of_" + name_of_film + ".jpg"
    #mean_frame=Image.open(mean_frame_path)

    for subdir, dirs, files in os.walk(orig_folder_path):
        for filename in files:
            if filename.find(name_of_film) != -1:
                curr_frame_path = subdir + "/" + filename

                curr_diff_frame_path =dest_folder_path+"/diff_"+filename
                subtract_images(curr_frame_path,mean_frame_path,curr_diff_frame_path,416,416)



if __name__ == "__main__":
    orig_folder_path = "D:/Amir/Machine_Learning_Course_Primrose/Final_Project/PCA_Process/input_frames"
    mean_frames_folder_path = "D:/Amir/Machine_Learning_Course_Primrose/Final_Project/PCA_Process/mean_frames"
    create_mean_images_dataset(orig_folder_path, mean_frames_folder_path, "Tia3_F_3", 416, 416)

    dest_folder_path= "D:/Amir/Machine_Learning_Course_Primrose/Final_Project/PCA_Process/diff_frames"
    create_delta_images(orig_folder_path, dest_folder_path, mean_frames_folder_path, "Tia3_F_3", 416, 416)





