import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from PIL import Image

save_path = "../data/ghudeki-cup-linear-algebra-and-group/"

def main():
    num_piece_width = 50
    num_piece_height = 29

    reds = []
    greens = []
    blues = []
    colors = []
    images = []
    for i in range(num_piece_width):
        for j in range(num_piece_height):
            file_path = f"{i}-{j}.jpg"
            img = mpimg.imread(save_path + file_path)
            img = img[3:-3,3:-3,:]

            r = np.mean(img[:,:,0])
            g = np.mean(img[:,:,1])
            b = np.mean(img[:,:,2])
            reds.append(r)
            greens.append(g)
            blues.append(b)
            colors.append([r, g, b])
            images.append(Image.open(save_path + file_path))
    
    reds = np.array(reds)
    greens = np.array(greens)
    blues = np.array(blues)
    colors = np.array(colors) / 255
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(reds, greens, blues, c=colors)
    plt.show()

    kmeans = KMeans(n_clusters=10).fit(colors)

    for i in range(10):
        os.makedirs(save_path + f"{i}")

    color_cnt = np.zeros(10)
    for i in range(colors.shape[0]):
        color_cnt[kmeans.labels_[i]] += 1
        images[i].save(save_path + f"{kmeans.labels_[i]}/{i}.jpg")

    print(color_cnt)


if __name__ == "__main__":
    main()