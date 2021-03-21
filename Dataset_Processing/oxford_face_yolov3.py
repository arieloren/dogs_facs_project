import numpy as np
import os
import shutil
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_txt(orig_path, dest_path):
    # convert xml to df:
    df_file = []
    tree = ET.parse(orig_path)
    root = tree.getroot()
    for member in root.findall('object'):
        value = (root.find('filename').text,
                 int(root.find('size')[0].text),
                 int(root.find('size')[1].text),
                 member[0].text,
                 int(member[4][0].text),
                 int(member[4][1].text),
                 int(member[4][2].text),
                 int(member[4][3].text)
                 )
        df_file.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(df_file, columns=column_name)
    for col in ['width', 'height', 'xmin', 'ymin', 'xmax', 'ymax']:
        xml_df[col] = xml_df[col].astype(int)

    # write the annotation to destination text file
    dest_file = open(dest_path, "w")
    for obj in xml_df.iterrows():
        cls = 0
        x_center = 0.5 * (obj[1]['xmax'] + obj[1]['xmin']) / float(obj[1]['width'])
        y_center = 0.5 * (obj[1]['ymax'] + obj[1]['ymin']) / float(obj[1]['height'])
        w = np.abs(obj[1]['xmax'] - obj[1]['xmin']) / float(obj[1]['width'])
        h = np.abs(obj[1]['ymax'] - obj[1]['ymin']) / float(obj[1]['height'])
        dest_file.write(str(cls) + " " + str(x_center) + " " + str(y_center) + " " + str(w) + " " + str(h) + "\n")
    dest_file.close()


def cat_xml_files_cleansing(orig_path, dest_path):
    for subdir, dirs, files in os.walk(orig_path):
        for filename in files:
            src_path = subdir + os.sep + filename
            if filename.islower():
                shutil.copy(src_path, dest_path)
                txt_path = dest_path + os.sep + filename[:-4] + ".txt"
                xml_to_txt(src_path, txt_path)


def cat_image_files_cleansing(orig_path, dest_path):
    for subdir, dirs, files in os.walk(orig_path):
        for filename in files:
            src_path = subdir + os.sep + filename
            print(filename[:-4])
            xml_path = dest_path + os.sep + filename[:-4] + ".xml"
            if (filename.islower() and os.path.isfile(xml_path)):
                shutil.copy(src_path, dest_path)


if __name__ == '__main__':
    orig_path = 'D:\\Amir\\Machine_Learning_Course_Primrose\\Final_Project\\oxford_dataset\\annotations\\xmls'
    dest_path = 'D:\\Amir\\Machine_Learning_Course_Primrose\\Final_Project\\preprocessed_dataset'
    cat_xml_files_cleansing(orig_path, dest_path)

    orig_path = 'D:\\Amir\\Machine_Learning_Course_Primrose\\Final_Project\\oxford_dataset\\images'
    cat_image_files_cleansing(orig_path, dest_path)
    z = 0
