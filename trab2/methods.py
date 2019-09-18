import numpy as np

def _global(image):
    img = np.copy(image)
    img = np.where(img < 128, 0, 255)
    return img

def min_max_in_neighborhood(image, delta, x, y):
    m = image[x-delta:x+delta+1, y-delta:y+delta+1]
    return (m.min(), m.max())
    
def _bernsen(image):
    img = np.copy(image)
    delta = 1
    for x in range(delta, img.shape[0]-delta):
        for y in range(delta, img.shape[1]-delta):
            (min, max) = min_max_in_neighborhood(image, delta, x, y)
            img[x][y] = (int(min) + int(max))/2
    return img