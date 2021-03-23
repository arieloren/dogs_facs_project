import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from PIL import Image


def collect_augmentations_names_for_file_name(kwargs):
    augmentations = ""
    for aug in kwargs:
        if aug.endswith("_range"):
            aug = aug[:-6]
        augmentations += aug
        augmentations += "-"
    return augmentations

def data_augmentation(directory, directory_destination, augmentation_statment, num_of_augmented_images,
                      **kwargs):
    # load the image
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            filepath = subdir + os.sep + filename
            image_location = os.path.dirname(filepath)
            if filepath.endswith(".jpg") or filepath.endswith(".png") or filepath.endswith(".jpeg"):
                img = load_img(filepath)
                img_name = os.path.basename(filepath)[:-4]
                # convert to numpy array
                data = img_to_array(img)
                # expand dimension to one sample
                samples = np.expand_dims(data, 0)
                if (augmentation_statment == True):

                    # create image data augmentation generator
                    datagen_1 = ImageDataGenerator(**kwargs)  # here enter the augmentation action you want
                    # prepare iterator
                    it_1 = datagen_1.flow(samples, batch_size=1)

                    # generate samples and plot
                    for i in range(num_of_augmented_images):
                        # generate batch of images
                        batch_1 = it_1.next()
                        # convert to unsigned integers for viewing
                        image_array_format_1 = batch_1[0].astype('uint8')
                        image_pil_format_1 = Image.fromarray(image_array_format_1)
                        os.chdir(directory_destination)
                        augmentations = collect_augmentations_names_for_file_name(kwargs)
                        image_pil_format_1.save(f"{img_name}--{augmentations}--augmentation-num{i}.jpg")


if __name__ == '__main__':
    directory = 'C:/Users/user/Documents/Ariel/DL_lab_project/dataset_procrssing/test_dataset'
    directory_destination = 'C:/Users/user/Documents/Ariel/DL_lab_project/dataset_procrssing/dest_test_dataset'
    augmentation_statment = True
    num_of_rotate_augmented_images = 6
    kwargs = {"rotation_range": 90, "width_shift_range": [-200, 200], "height_shift_range": 0.5}
    data_augmentation(directory, directory_destination, augmentation_statment, num_of_rotate_augmented_images, **kwargs)
