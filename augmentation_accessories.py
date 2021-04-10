from random import seed
from PIL import Image
from matplotlib import pyplot as plt
import cv2
import os


def visualize(image):
    plt.figure(figsize=(10, 10))
    plt.axis('off')
    plt.imshow(image)
    plt.show()


def plot_examples(images, bboxes=None, rows=5, columns=4):
    fig = plt.figure(figsize=(15, 15))

    for i in range(1, len(images)):
        if bboxes is not None:
            img = visualize_bbox(images[i - 1], bboxes[i - 1], class_name="Elon")
        else:
            img = images[i - 1]
        fig.add_subplot(rows, columns, i)
        plt.imshow(img)
    plt.show()


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

    return xmin, ymin, xmax, ymax


# From https://albumentations.ai/docs/examples/example_bboxes/
def visualize_bbox(img, bbox, class_name, color=(255, 0, 0), thickness=5):
    """Visualizes a single bounding box on the image"""
    x_min, y_min, x_max, y_max = yolo2voc(img, bbox)
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color, thickness)
    return img


def create_row(img, annot):
    row = []
    image_name=img.split("/")[-1]
    image = cv2.imread(img)
    height, width, _ = image.shape
    class_id = 0
    row.append(image_name)
    row.append(img)
    row.append(class_id)
    row.append(width)
    row.append(height)

    bboxes = []
    with open(annot, 'rt') as annots_file:
        annotations = annots_file.read().split("\n")
        for i in range(len(annotations)-1):
            attributes = annotations[i].split(" ")
            xc = float(attributes[1])
            yc = float(attributes[2])
            w = float(attributes[3])
            h = float(attributes[4])
            bbox = (xc, yc, w, h)
            bboxes.append(bbox)
    annots_file.close()

    row.append(bboxes)
    return row


def make_aug_per_image(img_n_ann_df, ind, transform):
    #seed(7)
    bboxes = img_n_ann_df.at[ind, 'bboxes']
    image_path = img_n_ann_df.at[ind, 'image_path']
    image = cv2.imread(image_path)
    augmentation = transform(image=image, bboxes=bboxes)
    return augmentation


def make_and_store_aug_per_image_folder(img_n_ann_df, transform, aug_per_images, aug_img_path, aug_ann_path):
    for ind in range(len(img_n_ann_df)):
        for j in range(1, aug_per_images + 1):
            augmentation = make_aug_per_image(img_n_ann_df, ind, transform)

            # save image:
            augmented_img = augmentation["image"]
            augmented_img_name = img_n_ann_df.at[ind,"image_name"].split("\\")[-1]
            extesion = augmented_img_name.split(".")[-1]
            image = Image.fromarray(augmentation["image"])
            image_saving_path = aug_img_path + "/" + augmented_img_name + "_#" + str(j) + "." + extesion
            image.save(image_saving_path)

            # save annotations:
            augmented_bboxes = augmentation["bboxes"]
            annotation_saving_path = aug_ann_path + "/" + augmented_img_name + "_#" + str(j) + ".txt"
            annots_file=open(annotation_saving_path,"w")
            for bbox in augmented_bboxes:
                class_id = img_n_ann_df.at[ind,"class_id"]
                xc = bbox[0]
                yc = bbox[1]
                w = bbox[2]
                h = bbox[3]
                ann = str(class_id) + " " + str(xc) + " " + str(yc) + " " + str(w) + " " + str(h) + "\n"
                annots_file.write(ann)
            annots_file.close()


# def data_augmentation(directory, directory_destination, augmentation_statment, num_of_rotate_augmented_images,
#                       **kwargs):
#     # load the image
#
#     for subdir, dirs, files in os.walk(directory):
#         for filename in files:
#             filepath = subdir + os.sep + filename
#             image_location = os.path.dirname(filepath)
#             if filepath.endswith(".jpg") or filepath.endswith(".png"):
#                 img = load_img(filepath)
#                 img_name = os.path.basename(filepath)[:-4]
#                 # convert to numpy array
#                 data = img_to_array(img)
#                 # expand dimension to one sample
#                 samples = np.expand_dims(data, 0)
#                 if (augmentation_statment == True):
#
#                     # create image data augmentation generator
#                     datagen_1 = ImageDataGenerator(kwargs)  # here enter the augmentation action you want
#                     # prepare iterator
#                     it_1 = datagen_1.flow(samples, batch_size=1)
#
#                     # generate samples and plot
#                     for i in range(num_of_rotate_augmented_images):
#                         # generate batch of images
#                         batch_1 = it_1.next()
#                         # convert to unsigned integers for viewing
#                         image_array_format_1 = batch_1[0].astype('uint8')
#
#                         image_pil_format_1 = Image.fromarray(image_array_format_1)
#                         os.chdir(directory_destination)
#                         image_pil_format_1.save(f"{img_name}_rotation_augmentation_num{i}.jpg")