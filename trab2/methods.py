import numpy as np

def max_in_neighborhood(size):
    delta = (size - 1) / 2
    [x-delta:x+delta+1] #[A, B)

def globalMethod(image):
    img = np.copy(image)
    img = np.where(img < 128, 0, 255)
    return img

def bernsenMethod(image):
    img = np.copy(image)
    return img