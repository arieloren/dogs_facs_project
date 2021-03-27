import cv2


def crop(orig_path, dest_path, annotation):
    # annotation=[x_c,y_c, w, h]
    image = cv2.imread(orig_path)
    height, width, _ = image.shape

    x_c = int(width * annotation[0])
    y_c = int(height * annotation[1])
    w = int(width * annotation[2])
    h = int(height * annotation[3])

    xmin = int(x_c - w / 2)
    ymin = int(y_c - h / 2)
    xmax = int(x_c + w / 2)
    ymax = int(y_c + h / 2)

    cropped_image = image[ymin:ymax, xmin:xmax]
    cv2.imwrite(dest_path, cropped_image)
