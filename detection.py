#!/usr/bin/python

import cv2
import numpy as np

def getResSize(img_screen_bgr):
    """Get resolution size of device's image.
    
    Args:
        img_bgr: 

    Returns:
        Height and width of screen

    Raises:
        ImageParseError:
    """
    pass

def getMoveCircleCoordinates():
    """Get move circle coordinates.

    Args:

    
    Returns:
        All move circle coordinates of screen

    Raises:
        ImageParseError:
        NotFoundError: If coordinates are not found.
    """
    pass

def getTempCoordinates(img_screen_bgr, img_temp_bgr, threshold):
    """Get coordinates of templated image on screen image.

    Args:
        img_screen_bgr: 
        img_temp_bgr:
        threshold:

    Returns:
        Center coordinates of screen
    
    Raises:
        ImageParseError: 
        NotFoundError: If coordinates are not found.
    """
    found = 0
    coords = np.array([])

    height, width = img_screen_bgr.shape[::-1]
    img_gray = cv2.cvtColor(img_screen_bgr, cv2.COLOR_BGR2GRAY)

    #normxcorr = cv2.matchTemplate(img_gray, temp_gray, cv2.TM_CCOEFF_NORMED)