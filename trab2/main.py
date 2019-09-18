import cv2
import sys
import os
import methods
from matplotlib import pyplot as plt

def readImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

def plotHistogram(img, title):
    plt.title(title)
    plt.xlabel('Valor do pixel')
    plt.ylabel('Quantidade')
    plt.hist(img)
    plt.show()

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    out_path = os.path.dirname(os.path.realpath(__file__)) + "/out/" + out_file
    image = readImage(in_file)

    if not os.path.exists("./out/"):
        os.makedirs("./out/")

    img = methods._global(image)
    plotHistogram(img, "Global Method")
    # cv2.imwrite(out_path + "_global.png", img)

    # img = methods._bernsen(image)
    # cv2.imwrite(out_path + "_bernsen.png", img)

    # img = methods._niblack(image)
    # cv2.imwrite(out_path + "_niblack.png", img)

    # img = methods._sauvola_pietaksinen(image)
    # cv2.imwrite(out_path + "_sauvola_pietaksinen.png", img)

    # img = methods._phansalskar(image)
    # cv2.imwrite(out_path + "_phansalskar.png", img)

    # img = methods._contrast(image)
    # cv2.imwrite(out_path + "_contrast.png", img)

    # img = methods._average(image)
    # cv2.imwrite(out_path + "_average.png", img)

    # img = methods._median(image)
    # cv2.imwrite(out_path + "_median.png", img)