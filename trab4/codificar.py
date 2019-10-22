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

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def replaceBits(num, bit, plano_bits):
    mask = 1 << plano_bits
    return (num & ~mask) | ((bit << plano_bits) & mask)

def writeTextOnImage(image_r, image_g, image_b, text, plano_bits):
    width = image_r.shape[0]
    height = image_r.shape[1]
    text_size = len(text)
    i = 0
    image = [image_r, image_g, image_b]
    for x in range(width):
        for y in range(height):
            if i == text_size:
                break
            image[i % 3][x][y] = replaceBits(image[i % 3][x][y], int(text[i]), plano_bits)
            i += 1
        if i == text_size:
            break
    return (image_r, image_g, image_b)

if __name__ == '__main__':
    in_file = sys.argv[1]
    in_text = sys.argv[2]
    plano_bits = int(sys.argv[3])
    out_file = sys.argv[4]
    out_path = "./out/"
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    # Read image and split RGB
    image = readImage(in_file)
    (image_r, image_g, image_b) = cv2.split(image)

    # Read text and convert to binary
    text = readText(in_text)
    text += "\0"
    text = text_to_bits(text)

    # Write text on image
    (image_r, image_g, image_b) = writeTextOnImage(image_r, image_g, image_b, text, plano_bits)
    image = cv2.merge((image_r, image_g, image_b))

    # Save image
    saveImage(out_path + out_file, image)