import numpy as np
import os
import imageio as io
from skimage import color
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


class Execute_PCA:
    def __init__(self, nComp, n_rows, n_cols):
        self.nComp = nComp
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.h = None
        self.w = None

    def read_images(self, path):
        X = []
        for root, dirs, files in os.walk(path, topdown=True):
            for name in files:
                full_file = os.path.join(root, name)
                if full_file.endswith(".jpg"):
                    img = io.imread(full_file)
                    self.h, self.w, _ = img.shape
                    X.append(color.rgb2gray(img).flatten())
                    # break
        X = np.array(X)
        return X

    def run_sklearn_pca(self, X_data, index):

        pca = PCA(n_components=self.nComp).fit(X_data)
        one_image = X_data[index]
        projections_on_eigenvectors = pca.transform(one_image.reshape(1, -1))
        reconstructed_img = pca.inverse_transform(projections_on_eigenvectors)
        eigenfaces = pca.components_.reshape([self.nComp, self.h, self.w])

        return one_image, reconstructed_img, eigenfaces

    def plot_images_compare(self, one_image, reconstructed_img):
        plt.imshow(reconstructed_img.reshape((self.h, self.w)), cmap=plt.cm.gray)
        plt.show()
        plt.imshow(one_image.reshape((self.h, self.w)), cmap=plt.cm.gray)
        plt.show()

    def plot_gallery(self, eigenfaces):
        eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]

        plt.figure(figsize=(1.8 * self.n_cols, 2.4 * self.n_rows))
        plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.9, hspace=0.35)
        # for i in range(n_row * n_col):
        for i in range(self.nComp):
            plt.subplot(self.n_rows, self.n_cols, i + 1)
            plt.imshow(eigenfaces[i].reshape((self.h, self.w)), cmap=plt.cm.gray)
            plt.title(eigenface_titles[i], size=12)
            plt.xticks(())
            plt.yticks(())
        plt.show()


if __name__ == "__main__":
    path = "D:/Amir/Machine_Learning_Course_Primrose/Final_Project/PCA_Process/diff_frames"
    pca_exec = Execute_PCA(10, 2, 5)
    X_data = pca_exec.read_images(path)
    one_image, reconstructed_img, eighenfaces = pca_exec.run_sklearn_pca(X_data, 5)
    pca_exec.plot_images_compare(one_image, reconstructed_img)
    pca_exec.plot_gallery(eighenfaces)
