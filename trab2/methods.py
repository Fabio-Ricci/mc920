import numpy as np
import math

# Auxiliar Methods
def min_max_in_neighborhood(image, delta, x, y):
    m = image[x-delta:x+delta+1, y-delta:y+delta+1]
    return (m.min(), m.max())

def localAverage(image, delta, x, y):
    m = image[x-delta:x+delta+1, y-delta:y+delta+1]
    n = (2*delta+1)**2
    return m.sum()/n

def standardDeviation(image, delta, x, y):
    m = image[x-delta:x+delta+1, y-delta:y+delta+1]
    return np.std(m)

def localMedian(image, delta, x, y):
    m = image[x-delta:x+delta+1, y-delta:y+delta+1]
    return np.median(m)

# Global Method
def _global(image):
    img = np.copy(image)
    img = np.where(img < 128, 0, 255)
    return img

# Bernsen Method   
def _bernsen(image):
    img = np.copy(image)
    hist = np.zeros(256)
    delta = 1
    for x in range(delta, img.shape[0]-delta):
        for y in range(delta, img.shape[1]-delta):
            (min, max) = min_max_in_neighborhood(image, delta, x, y)
            img[x][y] = (int(min) + int(max))/2
            hist[img[x][y]] = hist[img[x][y]] + 1
    return (img, hist)

# Niblack Method
def _niblack(image, delta=1, k=1):
    img = np.copy(image)
    hist = np.zeros(256)
    for x in range(delta, img.shape[0]-delta):
        for y in range(delta, img.shape[1]-delta):
            img[x][y] = localAverage(image, delta, x, y) + k*standardDeviation(image, delta, x, y)
            hist[img[x][y]] = hist[img[x][y]] + 1
    return (img, hist)

# Sauvola and Pietaksinen Method
def _sauvola_pietaksinen(image, delta=1, k=0.5, R=128):
    img = np.copy(image)
    hist = np.zeros(256)
    for x in range(delta, img.shape[0]-delta):
        for y in range(delta, img.shape[1]-delta):
            img[x][y] = localAverage(image, delta, x, y)*(1+k*(standardDeviation(image, delta, x, y)/R-1))
            hist[img[x][y]] = hist[img[x][y]] + 1
    return (img, hist)

# Phansalskar, More and Sabale Method
def _phansalskar(image, delta=1, k=0.25, R=0.5, p=2, q=10):
    img = np.copy(image)
    hist = np.zeros(256)
    for x in range(delta, img.shape[0]-delta):
        for y in range(delta, img.shape[1]-delta):
            avg = localAverage(image, delta, x, y)
            img[x][y] = avg*(1+p*math.exp(-q*avg)+k*(standardDeviation(image, delta, x, y)/R-1))
            hist[img[x][y]] = hist[img[x][y]] + 1
    return (img, hist)

# Contrast Method
def _contrast(image, delta=1):
    img = np.copy(image)
    hist = np.zeros(256)
    for x in range(delta, img.shape[0]-delta):
        for y in range(delta, img.shape[1]-delta):
            (min, max) = min_max_in_neighborhood(image, delta, x, y)
            img[x][y] = 255 if abs(int(min) - int(img[x][y])) < abs(int(max) - int(img[x][y])) else 0
            hist[img[x][y]] = hist[img[x][y]] + 1
    return (img, hist)

# Average Method
def _average(image, delta=1):
    img = np.copy(image)
    hist = np.zeros(256)
    for x in range(delta, img.shape[0]-delta):
        for y in range(delta, img.shape[1]-delta):
            avg = localAverage(image, delta, x, y)
            img[x][y] = 255 if img[x][y] > avg else 0
            hist[img[x][y]] = hist[img[x][y]] + 1
    return (img, hist)

# Median Method
def _median(image, delta=1):
    img = np.copy(image)
    hist = np.zeros(256)
    for x in range(delta, img.shape[0]-delta):
        for y in range(delta, img.shape[1]-delta):
            median = localMedian(image, delta, x, y)
            img[x][y] = 255 if img[x][y] > median else 0
            hist[img[x][y]] = hist[img[x][y]] + 1
    return (img, hist)