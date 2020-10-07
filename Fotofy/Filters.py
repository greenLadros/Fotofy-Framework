#ivri korem 2020
"""
The Filters class of the Fotofy Framework
"""

#import
import numpy as np
import cv2 as cv

#creating the class
class Filters():
    def reddify(self, img):
        """
        description
        """
        img[:,:,2] = 255
        return img
    def blueify(self, img):
        """
        description
        """
        img[:,:,0] = 255
        return img

    def greenify(self, img):
        """
        description
        """
        img[:,:,1] = 255
        return img
    
    def blur(self, img):
        """
        description
        """
        width, height, channels = np.shape(img)
        imgSmall = cv.resize(img, (32, 32), interpolation=cv.INTER_LINEAR)
        img = cv.resize(imgSmall, (height, width), interpolation=cv.INTER_NEAREST)  
        return img

    def coldChils(self, img):
        """
        description
        """
        img[:,:,0] = 200
        return img
    
    def warmVibes(self, img):
        """
        description
        """
        img[:,:,2] = 200
        return img

filters = Filters()
