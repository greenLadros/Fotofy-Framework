#ivri korem 2020
"""
The FileManager class in the Fotofy Framework
"""

#import
import os
import cv2 as cv

#creating the class
class FileManager():
    def saveImageAs(self, img, fileName):
        """
        description
        """
        cv.imwrite(fileName, img)

    def saveVideoAs(self, img, fileName):
        """
        description
        """
        pass

FileManager = FileManager()