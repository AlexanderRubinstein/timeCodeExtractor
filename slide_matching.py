import cv2
import numpy as np
from slide_extraction import FindCorners, FindCountour, ExtractSlide

def ShowMatching(image1, keypoints1, image2, keypoints2, matches):
    matching_image = cv2.drawMatchesKnn(image1, keypoints1, image2, keypoints2, matches, None, flags=2)
    ShowImage(matching_image)
    
def GetRatio(frame1, frame2, slide_extraction=True, ratio_coeff=0.75, show_matching=False):
    if slide_extraction:
        contour1 = FindCountour(frame1)
        slide1 = ExtractSlide(frame1, contour1)

        contour2 = FindCountour(frame2)
        slide2 = ExtractSlide(frame2, contour2)
    else:
        slide1 = frame1
        slide2 = frame2

    sift = cv2.xfeatures2d.SIFT_create()

    keypoints1, descriptors1 = sift.detectAndCompute(slide1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(slide2, None)
    
    if (len(keypoints1) < 2 or len(keypoints2) < 2):
        return -1
    
    bf = cv2.BFMatcher(cv2.NORM_L1)
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)

    # ratio test
    best_matches = []
    for m, n in matches:
        if m.distance < ratio_coeff*n.distance:
            best_matches.append([m])

    best_matches = sorted(best_matches, key = lambda x: x[0].distance)

    if show_matching:
        ShowMatching(slide1, keypoints1, slide2, keypoints2, best_matches)
    
    return 2.0 * len(best_matches) / (len(keypoints1) + len(keypoints2))
