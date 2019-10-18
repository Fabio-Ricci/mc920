import cv2
import sys
import os
import numpy as np

def readImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_COLOR)

def saveImage(filepath, image):
    cv2.imwrite(filepath, image)

def readText(in_text):
    text_file = open(in_text, "r")
    text = text_file.read([])
    text_file.close()
    return text

def readTextOnImage(image, text):
    return text

if __name__ == '__main__':
    in_file = sys.argv[1]
    plano_bits = sys.argv[2]
    out_file = sys.argv[3]
    out_path = os.path.dirname(os.path.realpath(__file__)) + "/out/" + out_file + "/"
    if not os.path.exists("./out/"):
        os.makedirs("./out/")
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    image = readImage(in_file)
    (image_r, image_g, image_b) = cv2.split(image)

    text = readTextOnImage(image)