import cv2
from resize_yolo_annotation import update_yolo_coordinates

# def crop(orig_path, dest_path, annotation):
#     # annotation=[x_c,y_c, w, h]
#     image = cv2.imread(orig_path)
#     height, width, _ = image.shape
#
#     x_c = int(width * annotation[0])
#     y_c = int(height * annotation[1])
#     w = int(width * annotation[2])
#     h = int(height * annotation[3])
#
#     xmin = int(x_c - w / 2)
#     ymin = int(y_c - h / 2)
#     xmax = int(x_c + w / 2)
#     ymax = int(y_c + h / 2)
#
#     cropped_image = image[ymin:ymax, xmin:xmax]
#     cv2.imwrite(dest_path, cropped_image)




def crop(orig_path, dest_path, annotation):
    # annotation=[x_c,y_c, w, h]
    image = cv2.imread(orig_path)
    height, width, _ = image.shape

    x_c = float(annotation[0])
    y_c = float(annotation[1])
    w = float(annotation[2])
    h = float(annotation[3])

    x_c, y_c, w, h = update_yolo_coordinates(x_c, y_c, w, h)

    x_c *= width
    y_c *= height
    w *= width
    h *= height

    xmin = int(x_c - w / 2)
    ymin = int(y_c - h / 2)
    xmax = int(x_c + w / 2)
    ymax = int(y_c + h / 2)

    cropped_image = image[ymin:ymax, xmin:xmax]
    cv2.imwrite(dest_path, cropped_image)

