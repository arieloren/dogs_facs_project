import numpy as np


def update_yolo_coordinates(xc, yc, w, h, rate_up=0.12, rate_down=0.3, rate_left=0.1, rate_right=0.15):
    # expand yolo coordinates:


    # if h * (1.0 + rate_down) > 1:
    #     h_new = 1.0
    #     delta_h = h_new - h
    #     yc_new = yc + 0.5 * delta_h
    # else:
    #     h_new = h * (1.0 + rate_down)
    #     yc_new = yc * (1.0 + 0.5 * rate_down)

    # h, yc
    h_new = h * (1 + rate_up + rate_down)
    yc_new = yc + 0.5 * h * (rate_down-rate_up)

    if yc_new - 0.5 * h_new < 0:
        exceed = np.abs(yc_new - 0.5 * h_new)
        h_new -= exceed
        yc_new += 0.5 * exceed
    elif yc_new + 0.5 * h_new > 1:
        exceed = np.abs(yc_new + 0.5 * h_new - 1)
        h_new -= exceed
        yc_new -= 0.5 * exceed

    # w, xc
    w_new = w * (1 + rate_left + rate_right)
    xc_new = xc + 0.5 * w * (rate_right-rate_left)

    if xc_new - 0.5 * w_new < 0:
        exceed = np.abs(xc_new - 0.5 * w_new)
        w_new -= exceed
        xc_new += 0.5 * exceed
    elif xc_new + 0.5 * w_new > 1:
        exceed = np.abs(xc_new + 0.5 * w_new - 1)
        w_new -= exceed
        xc_new -= 0.5 * exceed

    return xc_new, yc_new, w_new, h_new


def resize_annot(annot_path, dest_path):
    annots_file = open(annot_path, 'r')
    dest_file = open(dest_path, 'w')
    annots = annots_file.read().split("\n")
    for annot in annots:
        # annot = annot[:-1]
        annotation = annot.split(" ")
        cls = annotation[0]
        xc = float(annotation[1])
        yc = float(annotation[2])
        w = float(annotation[3])
        h = float(annotation[4])
        xc, yc, w, h = update_yolo_coordinates(xc, yc, w, h)
        dest_file.write("%s %.4f %.4f %.4f %.4f\n" % (cls, xc, yc, w, h))
    dest_file.close()
    annots_file.close()


if __name__ == "__main__":
    annot_path = "D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Dataset_Processing/ann.txt"
    dest_path = "D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Dataset_Processing/ann_new.txt"
    resize_annot(annot_path, dest_path)
