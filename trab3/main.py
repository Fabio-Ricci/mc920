import cv2
import sys
import os
import numpy as np
from matplotlib import pyplot as plt
from skimage.measure import label, regionprops

def readImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_COLOR)

def saveImage(filepath, image):
    cv2.imwrite(filepath, image)

def convertColors(image):
    (image_r, image_g, image_b) = cv2.split(img)
    for x in range(image.shape[0]):
       for y in range(image.shape[1]):
           img[x][y] = (int(image_r[x][y]) + int(image_g[x][y]) + int(image_b[x][y]))/3
    return img

def getEdges(image):
    img = cv2.Canny(image, 100, 200)
    return np.where(img == 0, 255, 0)

def getContours(image):  
    img = np.copy(image)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    ret, thresh = cv2.threshold(gray_image, 200, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    i = 0
    areas = np.zeros(len(contours) - 1)
    contours.reverse()
    contours = contours[1:]
    print("Número de regiões: ", len(contours), "\n") 
    for c in contours:
        # calculate moments for each contour
        M = cv2.moments(c)
        
        # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        cv2.putText(img, str(i), (cX-4, cY+4), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 0), 0)
        # Area
        areas[i] = cv2.contourArea(c)
        # Perimeter
        perimeter = round(cv2.arcLength(c, True), 6)
        # Eccentricity
        a1 = (M['mu20']+M['mu02'])/2
        a2 = np.sqrt(4*M['mu11']**2+(M['mu20']-M['mu02'])**2)/2
        minor_axis = a1-a2
        major_axis = a1+a2
        eccentricity = round(np.sqrt(1-minor_axis/major_axis), 6)
        # Solidity
        hull = cv2.convexHull(c)
        hull_area = cv2.contourArea(hull)
        solidity = round(float(areas[i])/hull_area, 6)

        print("Região", str(i) + ":", "área:", areas[i], "perímetro:", perimeter, "excentricidade:", eccentricity, "solidez:", solidity)
        i = i + 1
    return (img, areas)

def getAreasHistogram(areas, filepath):
    areasNumber = np.zeros(3)
    areasNumber[0] = len(areas[areas < 1500])
    areasNumber[1] = len([a for a in areas if a >= 1500 and a < 3000])
    areasNumber[2] = len(areas[areas >= 3000])
    print("número de regiões pequenas:", int(areasNumber[0]))
    print("número de regiões médias:", int(areasNumber[1]))
    print("número de regiões grandes:", int(areasNumber[2]))

    plt.title('Histograma de áreas dos objetos')
    plt.xlabel('Area')
    plt.ylabel('Número de Objetos')
    plt.hist(areas, bins=3)
    plt.savefig(filepath)

if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    out_path = os.path.dirname(os.path.realpath(__file__)) + "/out/" + out_file + "/"
    if not os.path.exists("./out/"):
        os.makedirs("./out/")
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    image = readImage(in_file)

    img = convertColors(image)
    saveImage(out_path + out_file + "_1.png", img)

    img = getEdges(img)
    saveImage(out_path + out_file + "_2.png", img)

    (img, areas) = getContours(image)
    saveImage(out_path + out_file + "_3.png", img)

    getAreasHistogram(areas, out_path + out_file + "_4.png")