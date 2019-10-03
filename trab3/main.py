import cv2
import sys
import os
from matplotlib import pyplot as plt

def readImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

def saveHistogram(image, title, path, filename):
    plt.title(title)
    plt.xlabel('Nível de cinza')
    plt.ylabel('Quantidade de pixels')
    plt.hist(image, bins=255)
    plt.savefig(path + filename + "_histogram")

if __name__ == '__main__':
    if not os.path.exists("./out/"):
        os.makedirs("./out/")
    if not os.path.exists(out_path):
        os.makedirs(out_path)
        
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    out_path = os.path.dirname(os.path.realpath(__file__)) + "/out/" + out_file + "/"
    image = readImage(in_file)