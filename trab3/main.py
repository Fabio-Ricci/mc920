import cv2
import sys
import os
import numpy as np
from matplotlib import pyplot as plt

def readImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_COLOR)

def printImage(filepath, image):
    cv2.imwrite(filepath, image)

def saveHistogram(image, title, path, filename):
    plt.title(title)
    plt.xlabel('Nível de cinza')
    plt.ylabel('Quantidade de pixels')
    plt.hist(image, bins=255)
    plt.savefig(path + filename + "_histogram")

def convertColors(image):
    img = np.copy(image)
    (image_r, image_g, image_b) = cv2.split(img)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            img[x][y] = (int(image_r[x][y]) + int(image_g[x][y]) + int(image_b[x][y]))/3
    return img

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    out_path = os.path.dirname(os.path.realpath(__file__)) + "/out/" + out_file + "/"
    if not os.path.exists("./out/"):
        os.makedirs("./out/")
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    image = readImage(in_file)
    img = convertColors(image)
    print(img)