import cv2
import sys
import os
import methods
from matplotlib import pyplot as plt

def readImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

def saveHistogram(image, title, out_path, methodName):
    plt.title(title)
    plt.xlabel('Valor do pixel')
    plt.ylabel('Quantidade de pixels')
    plt.hist(image, bins=255)
    plt.savefig(out_path + methodName + "_histogram")

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    out_path = os.path.dirname(os.path.realpath(__file__)) + "/out/" + out_file
    image = readImage(in_file)

    if not os.path.exists("./out/"):
        os.makedirs("./out/")

    img = methods._global(image)
    saveHistogram(img.flatten(), "Global Method", out_path, "_global")
    cv2.imwrite(out_path + "_global.png", img)

    img = methods._bernsen(image)
    saveHistogram(img.flatten(), "Bernsen Method", out_path, "_bernsen")
    cv2.imwrite(out_path + "_bernsen.png", img)

    img = methods._niblack(image)
    saveHistogram(img.flatten(), "Niblack Method", out_path, "_niblack")
    cv2.imwrite(out_path + "_niblack.png", img)

    img = methods._sauvola_pietaksinen(image)
    saveHistogram(img.flatten(), "Sauvola and Pietaksinen Method", out_path, "_sauvola_pietaksinen")
    cv2.imwrite(out_path + "_sauvola_pietaksinen.png", img)

    img = methods._phansalskar(image)
    saveHistogram(img.flatten(), "Phansalskar Method", out_path, "_phansalskar")
    cv2.imwrite(out_path + "_phansalskar.png", img)

    img = methods._contrast(image)
    saveHistogram(img.flatten(), "Contrast Method", out_path, "_contrast")
    cv2.imwrite(out_path + "_contrast.png", img)

    img = methods._average(image)
    saveHistogram(img.flatten(), "Average Method", out_path, "_average")
    cv2.imwrite(out_path + "_average.png", img)

    img = methods._median(image)
    saveHistogram(img.flatten(), "Median Method", out_path, "_median")
    cv2.imwrite(out_path + "_median.png", img)