import json
import pandas as pd


def convert_json_to_df(json_path, record_path):
    # load data using Python JSON module
    with open(json_path, 'r') as f:
        data = json.loads(f.read())
    f.close()
    # Normalizing data
    df = pd.json_normalize(data, record_path=record_path)

    return df


def create_annot_df(json_path):
    df_coordinates_confidence = convert_json_to_df(json_path, ['objects'])
    df_filename = convert_json_to_df(json_path, None)
    df_filename = df_filename["filename"]
    bounding_boxes_df = pd.concat([df_filename, df_coordinates_confidence], axis=1)
    bounding_boxes_df = bounding_boxes_df.rename(columns={"filename": "filepath"})
    bounding_boxes_df = bounding_boxes_df.fillna(method='ffill')
    bounding_boxes_df = bounding_boxes_df.sort_values(["filepath", "confidence"], ascending=[True, False])
    idx = bounding_boxes_df.groupby(['filepath'])['confidence'].transform(max) == bounding_boxes_df['confidence']
    bounding_boxes_df = bounding_boxes_df[idx]
    bounding_boxes_df = bounding_boxes_df.reset_index()
    bounding_boxes_df=bounding_boxes_df.drop(["index"], axis=1)
    return bounding_boxes_df


if __name__ == '__main__':
    json_path = 'D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Crop_Handling/our_images.json'
    bounding_boxes_df = create_annot_df(json_path)
    #bounding_boxes_df.to_csv("D:\\Amir\\Machine_Learning_Course_Primrose\\Final_Project\\Crop_Handling\\bounding_boxes.csv")
    z = 0
