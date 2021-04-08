class_labels = ["Face"]
import albumentations as A
import cv2


# extraction the bounding boxes per image
def create_boxes_list(bboxes_path):
    bboxes = []
    bboxes_file = open(bboxes_path, "r")
    # split to rows:
    rows = bboxes_file.read().split("\n")
    for i in range(len(rows) - 1):
        # split to attributes:
        attributes = rows[i].split(" ")
        xc = float(attributes[1])
        yc = float(attributes[2])
        w = float(attributes[3])
        h = float(attributes[4])
        bbox = [xc, yc, w, h]
        # bbox = attributes[1:].astype(float)
        bboxes.append(bbox)
    return bboxes


def yolo2voc(image, bbox):
    # annotation=[x_c,y_c, w, h]
    height, width, _ = image.shape

    x_c = float(bbox[0])
    y_c = float(bbox[1])
    w = float(bbox[2])
    h = float(bbox[3])

    x_c *= width
    y_c *= height
    w *= width
    h *= height

    xmin = int(x_c - w / 2)
    ymin = int(y_c - h / 2)
    xmax = int(x_c + w / 2)
    ymax = int(y_c + h / 2)

    return [xmin, ymin, xmax, ymax]


def create_aug_transforms(lim_angle, image, bboxes):
    transformed_image_aug = []
    transformed_bboxes_aug = []
    transformed_class_labels_aug = []
    #for p_horizeflip in [0, 1]:
    for p_rotate in [0, 1]:
        # transform = A.Compose([A.HorizontalFlip(p=p_horizeflip),
        #                        A.Rotate(limit=lim_angle, always_apply=True, p=p_rotate)],
        #                       bbox_params=A.BboxParams(format='yolo', min_area=1024, min_visibility=0.1, label_fields=['class_labels']))
        transform = A.Compose([A.Rotate(limit=lim_angle, always_apply=True, p=p_rotate)],
                              bbox_params=A.BboxParams(format='yolo', min_area=1024, min_visibility=0.1,label_fields=['class_labels']))

        transformed = transform(image=image, bboxes=bboxes, class_labels=class_labels)

        transformed_image = transformed['image']
        transformed_image_aug.append(transformed_image)

        transformed_bboxes = transformed['bboxes']
        transformed_bboxes_aug.append(transformed_bboxes)

        transformed_class_labels = transformed['class_labels']
        transformed_class_labels_aug.append(transformed_class_labels)

        transformed_bboxes_voc_aug = []
        for bboxes_bandle in transformed_bboxes_aug:
            for bbox in bboxes_bandle:
                bbox_voc = yolo2voc(image, bbox)
                transformed_bboxes_voc_aug.append(bbox_voc)


    return transformed_image_aug, transformed_bboxes_aug, transformed_class_labels_aug, transformed_bboxes_voc_aug


# augmentation transform
# transform = A.Compose([
#     A.HorizontalFlip(p=0.5),
#     A.RandomBrightnessContrast(p=0.2),
# ], bbox_params=A.BboxParams(format='yolo', min_area=1024, min_visibility=0.1, label_fields=['class_labels']))


# aug. for a whole folder

# def create_augmentation(orig_path, dest_path):
#     for subdir, dirs, files in os.walk(orig_path):
#         for filename in files:
#             image = cv2.imread(orig_path)
#             image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

img_path = 'D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Augmentation_Dog_Face/frames/imgs/n02099712_7775.jpg'
ann_path = 'D:/Amir/Machine_Learning_Course_Primrose/Final_Project/Augmentation_Dog_Face/frames/annots/n02099712_7775.txt'

image = cv2.imread(img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

bboxes = create_boxes_list(ann_path)
# transformed = transform(image=image, bboxes=ann, class_labels=class_labels)
# transformed_image = transformed['image']
# transformed_bboxes = transformed['bboxes']
# transformed_class_labels = transformed['class_labels']


transformed_image_aug, transformed_bboxes_aug, transformed_class_labels_aug, bboxes_voc = create_aug_transforms(90,
                                                                                                                image,
                                                                                                                bboxes)
cv2.imwrite()
z=0