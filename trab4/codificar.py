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
    text = text_file.read()
    text_file.close()
    return text

def writeTextOnImage(image_r, image_g, image_b, text, plano_bits):
    width = image_r.shape[0]
    height = image_r.shape[1]
    # for i in range(0, width):
    #     for i in range(0, height):

    return (image_r, image_g, image_b)

if __name__ == '__main__':
    in_file = sys.argv[1]
    in_text = sys.argv[2]
    plano_bits = sys.argv[3]
    out_file = sys.argv[4]
    out_path = os.path.dirname(os.path.realpath(__file__)) + "/out/" + out_file + "/"
    if not os.path.exists("./out/"):
        os.makedirs("./out/")
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    # Read image and split RGB
    image = readImage(in_file)
    (image_r, image_g, image_b) = cv2.split(image)

    # Read text and convert to ASCII
    text = [ord(c) for c in readText(in_text)]

    # Write text on image
    (image_r, image_g, image_b) = writeTextOnImage(image_r, image_g, image_b, text, plano_bits)
    image = cv2.merge((image_r, image_g, image_b))

    # Save image
    saveImage(out_path + out_file + ".png", image)