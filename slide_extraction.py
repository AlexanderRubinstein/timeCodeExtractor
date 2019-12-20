import cv2
import matplotlib.pyplot as plt
import numpy as np
import operator

def DisplayPoints(image, points, radius=5, colour=(0, 0, 255)):
    img = image.copy()

    if len(colour) == 3:
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif img.shape[2] == 1:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    for point in points:
        img = cv2.circle(img, tuple(int(x) for x in point), radius, colour, -1)

    plt.imshow(img, 'gray')

def PreprocessImage(image):
    processed = cv2.GaussianBlur(image.copy(), (9, 9), 0)
    processed = cv2.adaptiveThreshold(processed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    processed = cv2.bitwise_not(processed, processed)

    return processed

def distance(p1, p2):
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    
    return np.sqrt((a ** 2) + (b ** 2))

def FindCountour(image):
    processed = PreprocessImage(image)
    _, ext_contours, _ = cv2.findContours(processed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(ext_contours, key=cv2.contourArea)
    contour = contour.squeeze()
    
    return contour

def FindCorners(corners):
    bottom_right, _ = max(enumerate([corner[0] + corner[1] for corner in corners]), key=operator.itemgetter(1))
    top_left, _ = min(enumerate([corner[0] + corner[1] for corner in corners]), key=operator.itemgetter(1))
    bottom_left, _ = min(enumerate([corner[0] - corner[1] for corner in corners]), key=operator.itemgetter(1))
    top_right, _ = max(enumerate([corner[0] - corner[1] for corner in corners]), key=operator.itemgetter(1))
    
    return [corners[top_left], corners[top_right], corners[bottom_right], corners[bottom_left]]
    
def ExtractSlide(image, contour):
    corners = FindCorners(contour)
    
    src = np.array(corners, dtype='float32')
   
    side = max([distance(corners[3], corners[0]),
                distance(corners[1], corners[2]),
                distance(corners[3], corners[2]),
                distance(corners[1], corners[0])
    ])
    
    dst = np.array([[0, 0], [side - 1, 0], [side - 1, side - 1], [0, side - 1]], dtype='float32')
    img = cv2.getPerspectiveTransform(src, dst)
    img = cv2.warpPerspective(image, img, (int(side), int(side)))
    
    return img
