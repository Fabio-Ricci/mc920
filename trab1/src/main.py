import cv2
import numpy as np
import matplotlib.pyplot as plt

def readColorImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_COLOR) 

def readGreyImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

def showImage(image):
    plt.imshow(image, cmap="gray", vmin=0, vmax=255)
    plt.show()

def halftoning(image):
    f = np.copy(image)
    width = f.shape[1]
    height = f.shape[0]
    g = np.zeros((width, height))
    for x in range(0, width):
        for y in range(0, height):
            if f[x][y] < 128:
                g[x][y] = 0
            else:
                g[x][y] = 1
            error = f[x][y] - g[x][y]*255

            f[x][y] = 0
            if x + 1 < width:
                f[x+1][y] += (7/16)*error
            if x - 1 > 0 and y + 1 < height:
                f[x-1][y+1] += (3/16)*error
            if y + 1 < height:
                f[x][y+1] += (5/16)*error
            if x + 1 < width and y + 1 < height:
                f[x+1][y+1] += (1/16)*error

    g = np.multiply(g, 255)
    return (f, g)

def halftoningAlternating(image):
    f = np.copy(image)
    width = f.shape[1]
    height = f.shape[0]
    g = np.zeros((width, height))
    i = 0
    for x in range(0, width):
        if i % 2 == 0: #going right
            for y in range(0, height):
                if f[x][y] < 128:   
                    g[x][y] = 0
                else:
                    g[x][y] = 1
                error = f[x][y] - g[x][y]*255

                f[x][y] = 0
                if x + 1 < width:
                    f[x+1][y] += (7/16)*error
                if x - 1 > 0 and y + 1 < height:
                    f[x-1][y+1] += (3/16)*error
                if y + 1 < height:
                    f[x][y+1] += (5/16)*error
                if x + 1 < width and y + 1 < height:
                    f[x+1][y+1] += (1/16)*error
        else:
            for y in range(height, 0, -1):
                if f[x][y] < 128:
                    g[x][y] = 0
                else:
                    g[x][y] = 1
                error = f[x][y] - g[x][y]*255

                f[x][y] = 0
                if x -1 < 0:
                    f[x-1][y] += (7/16)*error
                if x + 1 < width and y + 1 < height:
                    f[x+1][y+1] += (3/16)*error
                if y + 1 < height:
                    f[x][y+1] += (5/16)*error
                if x - 1 < 0 and y + 1 < height:
                    f[x-1][y+1] += (1/16)*error
    
    g = np.multiply(g, 255)
    return (f, g)

if __name__ == '__main__':
    image = readColorImage("../in/baboon.png")

    # original = np.zeros(shape=image.shape)
    # binary = np.zeros(shape=image.shape)
    # for i in range(3):
    #     (original[i], binary[i]) = halftoning(image[i])

    # image = readGreyImage("../in/baboon.png")
    # #Halftoning
    # (original, binary) = halftoning(image)
    # showImage(original)
    # showImage(binary)

    # #Halftoning Alternating
    # (original, binary) = halftoningAlternating(image)
    # showImage(original)
    # showImage(binary)