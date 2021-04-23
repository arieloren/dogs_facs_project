import numpy as np
import os
import imageio as io
from skimage import color
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# path = r'C:\Users\primrose\Downloads\faces94\faces94'
path = 'D:\\Amir\\Machine_Learning_Course_Primrose\\Final_Project\PCA_Process\\diff_frames'

# h = 416
# w = 416
def read_images(path):
    X = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            full_file = os.path.join(root, name)
            if full_file.endswith(".jpg"):
                img = io.imread(full_file)
                h, w, _ = img.shape
                X.append(color.rgb2gray(img).flatten())
                #break
    X = np.array(X)

    return X, h, w


# establish the pca

def run_sklearn_pca(X_data, h, w, n_components=10):
    pca = PCA(n_components=n_components).fit(X_data)
    one_image = X_data[0]
    projections_on_eigenvectors = pca.transform(one_image.reshape(1, -1))
    reconstructed_img = pca.inverse_transform(projections_on_eigenvectors)
    eigenfaces = pca.components_.reshape([n_components, h, w])

    return one_image, reconstructed_img, eigenfaces


def plot_images_compare(one_image, reconstructed_img, h, w):
    plt.imshow(reconstructed_img.reshape((h, w)), cmap=plt.cm.gray)
    plt.show()
    plt.imshow(X_data[0].reshape((h, w)), cmap=plt.cm.gray)
    plt.show()


def plot_gallery(eigenfaces):
    eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]

    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.9, hspace=0.35)
    for i in range(self.nComp):
        plt.subplot(n_rows, self.n_cols, i + 1)
        #eigenfaces[i]=eigenfaces[i].squeeze()
        plt.xticks(())
        plt.yticks(())
        plt.imshow(eigenfaces[:,:,i], cmap=plt.cm.gray)
        plt.title((eigenface_titles[i]), size=12)

    plt.show()


X_data,h,w = read_images(path)
one_image, reconstructed_img,eighenfaces = run_sklearn_pca(X_data,h,w)
plot_images_compare(one_image,reconstructed_img,h,w)
plot_gallery(eighenfaces,h,w,3,5)
