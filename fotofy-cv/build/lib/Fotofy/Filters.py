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
        this is reddify filter

        Parameters:
        img(matrix): the target image;

        Returnes:
        (matrix): the img with the filter;
        """
        img[:,:,2] = 255
        return img
    def blueify(self, img):
        """
        this is blueify filter

        Parameters:
        img(matrix): the target image;

        Returnes:
        (matrix): the img with the filter;
        """
        img[:,:,0] = 255
        return img

    def greenify(self, img):
        """
        this is greenify filter

        Parameters:
        img(matrix): the target image;

        Returnes:
        (matrix): the img with the filter;
        """
        img[:,:,1] = 255
        return img
    
    def blur(self, img):
        """
        this is blur filter

        Parameters:
        img(matrix): the target image;

        Returnes:
        (matrix): the img with the filter;
        """
        width, height, channels = np.shape(img)
        imgSmall = cv.resize(img, (32, 32), interpolation=cv.INTER_LINEAR)
        img = cv.resize(imgSmall, (height, width), interpolation=cv.INTER_NEAREST)  
        return img

    def coldChils(self, img):
        """
        this is coldChils filter

        Parameters:
        img(matrix): the target image;

        Returnes:
        (matrix): the img with the filter;
        """
        img[:,:,0] = 200
        return img
    
    def warmVibes(self, img):
        """
        this is warmVibes filter

        Parameters:
        img(matrix): the target image;

        Returnes:
        (matrix): the img with the filter;
        """
        img[:,:,2] = 200
        return img

Filters = Filters()
