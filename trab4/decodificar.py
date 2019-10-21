import cv2
import sys
import os
import numpy as np
import binascii

MAX_TEXT_SIZE = 8

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

def readBit(num, plano_bits):
    return num >> plano_bits & 1

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def readTextOnImage(image_r, image_g, image_b, plano_bits):
    width = image_r.shape[0]
    height = image_r.shape[1]
    text_size = ""
    text = ""
    i = 0
    x = 0
    y = 0
    for x in range(width):
        for y in range(height):
            if i == MAX_TEXT_SIZE:
                break
            text_size += str(readBit(image_r[x][y], plano_bits))
            i += 1
            if i == MAX_TEXT_SIZE:
                break
            text_size += str(readBit(image_g[x][y], plano_bits))
            i += 1
            if i == MAX_TEXT_SIZE:
                break
            text_size += str(readBit(image_b[x][y], plano_bits))
            i += 1
        if i == MAX_TEXT_SIZE:
            break    
    text_size = decode_binary_string(text_size)
    for x in range(x, width):
        for y in range(y, height):
            if i == text_size:
                break
            text += str(readBit(image_r[x][y], plano_bits))
            i += 1
            if i == text_size:
                break
            text += str(readBit(image_g[x][y], plano_bits))
            i += 1
            if i == text_size:
                break
            text += str(readBit(image_b[x][y], plano_bits))
            i += 1
        if i == text_size:
            break
    return decode_binary_string(text[:30])

if __name__ == '__main__':
    in_file = sys.argv[1]
    image_name = in_file[:-4]
    plano_bits = int(sys.argv[2])
    out_file = sys.argv[3]

    # Read the coded image
    image = readImage(in_file)
    (image_r, image_g, image_b) = cv2.split(image)

    # Extract text from image
    text = readTextOnImage(image_r, image_g, image_b, plano_bits)
    print(text)

    # Save the text on file
    saveText(out_file, text)