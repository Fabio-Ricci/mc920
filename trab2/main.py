import cv2
import sys
import os
import methods
from matplotlib import pyplot as plt

def readImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

def saveHistogram(hist, title, out_path, methodName, weights=None):
    plt.title(title)
    plt.xlabel('Valor do pixel')
    plt.ylabel('Quantidade')
    plt.hist(hist, weights=weights, bins=255)
    plt.savefig(out_path + methodName + "_histogram")

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    out_path = os.path.dirname(os.path.realpath(__file__)) + "/out/" + out_file
    image = readImage(in_file)

    if not os.path.exists("./out/"):
        os.makedirs("./out/")

    img = methods._global(image)
    saveHistogram(img, "Global Method", out_path, "_global")
    cv2.imwrite(out_path + "_global.png", img)

    (img, hist) = methods._bernsen(image)
    saveHistogram(hist, "Bernsen Method", out_path, "_bernsen", weights=hist)
    cv2.imwrite(out_path + "_bernsen.png", img)

    (img, hist) = methods._niblack(image)
    saveHistogram(hist, "Niblack Method", out_path, "_niblack", weights=hist)
    cv2.imwrite(out_path + "_niblack.png", img)

    (img, hist) = methods._sauvola_pietaksinen(image)
    saveHistogram(hist, "Sauvola and Pietaksinen Method", out_path, "_sauvola_pietaksinen", weights=hist)
    cv2.imwrite(out_path + "_sauvola_pietaksinen.png", img)

    (img, hist) = methods._phansalskar(image)
    saveHistogram(hist, "Phansalskar Method", out_path, "_phansalskar", weights=hist)
    cv2.imwrite(out_path + "_phansalskar.png", img)

    (img, hist) = methods._contrast(image)
    saveHistogram(hist, "Contrast Method", out_path, "_contrast", weights=hist)
    cv2.imwrite(out_path + "_contrast.png", img)

    (img, hist) = methods._average(image)
    saveHistogram(hist, "Average Method", out_path, "_average", weights=hist)
    cv2.imwrite(out_path + "_average.png", img)

    (img, hist) = methods._median(image)
    saveHistogram(hist, "Median Method", out_path, "_median", weights=hist)
    cv2.imwrite(out_path + "_median.png", img)