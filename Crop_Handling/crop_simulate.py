import pandas as pd
import cv2
from crop_by_coordinates import crop
bb_df = pd.read_csv("D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Crop_Handling/bounding_boxes.csv")
print(bb_df)
for i, row in bb_df.iterrows():
    isDuplicate=False
    orig_path = row["filepath"]
    output_name = "crop_" + orig_path.split("/")[-1]
    dest_path = "D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Crop_Handling/output_our_images/" + output_name
    xc = row["relative_coordinates.center_x"]
    yc = row["relative_coordinates.center_y"]
    w = row["relative_coordinates.width"]
    h = row["relative_coordinates.height"]
    annotation=[xc,yc,w,h]
    crop(orig_path, dest_path, annotation)

s = 0
