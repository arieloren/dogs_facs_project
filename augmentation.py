# imports:
import os
import glob
import cv2
import albumentations as A
import pandas as pd
import numpy as np
from augmentation_accessories import create_row, make_and_store_aug_per_image_folder, yolo2voc
import matplotlib.pyplot as plt
from PIL import Image

# upload annotations and their images
os.chdir('D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Augmentation_Dog_Face/frames/annots')
annots = glob.glob('D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Augmentation_Dog_Face/frames/annots/*')
imgs = glob.glob('D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Augmentation_Dog_Face/frames/imgs/*')

# create dataframe of annotations
final_df = []
for img, annots in zip(imgs, annots):
    row = create_row(img, annots)
    final_df.append(row)
df = pd.DataFrame(final_df, columns=['image_name', 'image_path', 'class_id', 'width', 'height', 'bboxes'])
df.to_csv(
    "D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Augmentation_Dog_Face/frames/images_and_their_annotations.csv",
    index=False)

# augmentation function
transform = A.Compose(
    [
        A.Resize(width=1920, height=1080),
        A.RandomCrop(width=1280, height=720),
        A.Rotate(limit=40, p=0.9, border_mode=cv2.BORDER_CONSTANT),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.1),
        A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.9),
        A.OneOf([
            A.Blur(blur_limit=3, p=0.5),
            A.ColorJitter(p=0.5),
        ], p=1.0),
    ], bbox_params=A.BboxParams(format="yolo", min_area=2048,
                                min_visibility=0.3, label_fields=[])
)
aug_img_path = 'D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Augmentation_Dog_Face/frames/augs'
aug_ann_path = 'D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Augmentation_Dog_Face/frames/augs'

make_and_store_aug_per_image_folder(df, transform, 15, aug_img_path, aug_ann_path)
image = cv2.imread(
    "D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Augmentation_Dog_Face/frames/augs/n02099712_6586.jpg_#11.jpg")
annots = "D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Augmentation_Dog_Face/frames/augs/n02099712_6586.jpg_#11.txt"
with open(annots, 'rt') as annots_file:
    bboxes = []
    annotations = annots_file.read().split("\n")
    for i in range(len(annotations) - 1):
        attributes = annotations[i].split(" ")
        xc = float(attributes[1])
        yc = float(attributes[2])
        w = float(attributes[3])
        h = float(attributes[4])
        bbox = (xc, yc, w, h)
        bboxes.append(bbox)
annots_file.close()
xmin, ymin, xmax, ymax = yolo2voc(image, bboxes[0])
cv2.rectangle(image,(xmin, ymin),(xmax, ymax),color=(255, 0, 0), thickness=5)
plt.imshow(image)
plt.show()