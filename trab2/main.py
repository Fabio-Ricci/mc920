import cv2
import sys
import os
import methods
from matplotlib import pyplot as plt

def readImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

def saveHistogram(image, title, path, file):
    plt.title(title)
    plt.xlabel('Nível de cinza')
    plt.ylabel('Quantidade de pixels')
    plt.hist(image, bins=255)
    plt.savefig(path + file + "_histogram")

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    out_path = os.path.dirname(os.path.realpath(__file__)) + "/out/" + out_file + "/"
    image = readImage(in_file)

    if not os.path.exists("./out/"):
        os.makedirs("./out/")
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    saveHistogram(image.flatten(), "Original Image", out_path, out_file)

    img = methods._global(image)
    # saveHistogram(img.flatten(), "Global Method", out_path, "_global")
    cv2.imwrite(out_path + out_file + "_global.png", img)

    delta = 3
    img = methods._niblack(image, delta=delta)
    # saveHistogram(img.flatten(), "Niblack Method", out_path, "_niblack")
    cv2.imwrite(out_path + out_file + "_niblack.png", img)

    delta = 2
    img = methods._bernsen(image, delta=delta)
    img = img[delta:img.shape[0]-delta, delta:img.shape[1]-delta]
    # saveHistogram(img.flatten(), "Bernsen Method", out_path, "_bernsen")
    cv2.imwrite(out_path + out_file + "_bernsen.png", img)

    img = methods._sauvola_pietaksinen(image, delta=delta)
    img = img[delta:img.shape[0]-delta, delta:img.shape[1]-delta]
    # saveHistogram(img.flatten(), "Sauvola and Pietaksinen Method", out_path, "_sauvola_pietaksinen")
    cv2.imwrite(out_path + out_file + "_sauvola_pietaksinen.png", img)

    img = methods._phansalskar(image, delta=delta)
    img = img[delta:img.shape[0]-delta, delta:img.shape[1]-delta]
    # saveHistogram(img.flatten(), "Phansalskar Method", out_path, "_phansalskar")
    cv2.imwrite(out_path + out_file + "_phansalskar.png", img)

    img = methods._contrast(image, delta=delta)
    img = img[delta:img.shape[0]-delta, delta:img.shape[1]-delta]
    # saveHistogram(img.flatten(), "Contrast Method", out_path, "_contrast")
    cv2.imwrite(out_path + out_file + "_contrast.png", img)

    img = methods._average(image, delta=delta)
    img = img[delta:img.shape[0]-delta, delta:img.shape[1]-delta]
    # saveHistogram(img.flatten(), "Average Method", out_path, "_average")
    cv2.imwrite(out_path + out_file + "_average.png", img)

    img = methods._median(image, delta=delta)
    img = img[delta:img.shape[0]-delta, delta:img.shape[1]-delta]
    # saveHistogram(img.flatten(), "Median Method", out_path, "_median")
    cv2.imwrite(out_path + out_file + "_median.png", img)