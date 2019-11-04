import cv2
import sys
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import math

def readImage(filepath):
    return cv2.imread(filepath, cv2.IMREAD_COLOR)

def saveImage(filepath, image):
    cv2.imwrite(filepath, image)

def svd(f, k):
    f = np.moveaxis(f, -1, 0)
    u, s, vh = np.linalg.svd(f[:, :, 0], full_matrices=False)
    g = u @ s[..., None, :] @ vh
    # SVD for all 3 channels
    u_b, s_b, vh_b = np.linalg.svd(f[:, :, 0], full_matrices=False)
    u_g, s_g, vh_g = np.linalg.svd(f[:, :, 1], full_matrices=False)
    u_r, s_r, vh_r = np.linalg.svd(f[:, :, 2], full_matrices=False)
    u = np.dstack((u_b, u_g, u_r))
    s = np.dstack((np.diag(s_b), np.diag(s_g), np.diag(s_r)))
    vh = np.dstack((vh_b, vh_g, vh_r))
    # Consider only k components
    u = u[:, :k, :]
    s = s[:k, :k, :]
    vh = vh[:k, :, :]
    g_b = u[:, :, 0] @ s[:, :, 0] @ vh[:, :, 0]
    g_g = u[:, :, 1] @ s[:, :, 1] @ vh[:, :, 1]
    g_r = u[:, :, 2] @ s[:, :, 2] @ vh[:, :, 2]
    return cv2.merge((g_b, g_g, g_r))

if __name__ == '__main__':
    in_file = sys.argv[1]
    k = int(sys.argv[2])
    out_file = sys.argv[3]
    out_path = "./out/"
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    # Read image
    image = readImage(in_file)

    # Calculate PCA
    img = svd(image, k)

    # Calculate RMSE

    # Save image
    saveImage(out_path + out_file, img)