import cv2
import sys
import os
import numpy as np
import string

def readImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_COLOR)

def saveImage(filepath, image):
    cv2.imwrite(filepath, image)

def readText(in_text):
    text_file = open(in_text, "r")
    text = text_file.read([])
    text_file.close()
    return text

def saveText(filepath, text):
    f = open(filepath, "w+")
    f.write(text)
    f.close()

def decode_binary_string(s):
    text = ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
    text = text[:text.find('\0')]
    return ''.join(filter(lambda x: x in set(string.printable), text))

def readTextOnImage(image_b, image_g, image_r, plano_bits):
    text = ""
    image = [image_b, image_g, image_r]
    # Preserve only the coded bit
    image = np.bitwise_and(image, 1 << plano_bits)
    # Shift right to get 0 or 1
    image = np.right_shift(image, plano_bits)
    zero_count = 0
    i = 0
    for x in range(image[0].shape[0]):
        for y in range(image[0].shape[1]):
            text += str(image[0][x][y])
            text += str(image[1][x][y])
            text += str(image[2][x][y])
    return decode_binary_string(text)

if __name__ == '__main__':
    in_file = sys.argv[1]
    plano_bits = int(sys.argv[2])
    out_file = sys.argv[3]
    out_path = "./out/"
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    # Read the coded image
    image = readImage(in_file)
    (image_b, image_g, image_r) = cv2.split(image)

    # Extract text from image
    text = readTextOnImage(image_b, image_g, image_r, plano_bits)

    # Save the text on file
    saveText(out_path + out_file, text)