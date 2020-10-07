#ivri korem 2020
"""
The Brush class of the Fotofy Framework
"""

#import
import numpy as np
import cv2 as cv

#creating the class
class Brush():
    def drawBox(self, img, pt1, pt2, color=(0, 255, 0), thickness=3):
        """
        description
        """
        try:
            cv.rectangle(img, pt1, pt2, color, thickness)
        except:
            print('failed to draw')

    def drawCircle(self, img, center, radius=25, color=(0, 255, 0), thickness=3):
        """
        description
        """
        try:
            return cv.circle(img, center, radius, color, thickness)
        except:
            print('failed to draw')

    def drawLine(self, img, pt1 ,pt2, color=(0, 255, 0), thickness=3):
        """
        description
        """
        try:
            return cv.line(img, pt1, pt2, color, thickness)
        except:
            print('failed to draw') 
    
    def drawText(self, img, loc, text="Hello World!", font=cv.FONT_HERSHEY_SIMPLEX, fontSize=25, color=(0, 255, 0), thickness=3):
        """
        description
        """
        try:
            return cv.putText(img, text, loc, font, fontSize, color, thickness)
        except:
            print('failed to draw')
    
    def drawPixels(self, img, pixelsMatrix, isConnected=True, color=(0, 255, 0), thickness=3):
        """
        description
        """
        try:
            vertices = np.array(pixelsMatrix, dtype=np.int32)
            pts = vertices.reshape((-1, 1, 2))
            return cv.polylines(img, [pts], isConnected, color, thickness)
        except:
            print('failed to draw')

    def createBlankImage(self, width=250, height=250, color='black'):
        """
        description
        """
        #creating black blank image
        blankImg = np.zeros(shape=(width, height, 3), dtype=np.int16)
        if color == 'black':
            return blankImg
        elif color == 'white':
            blankImg[:,:,:] = 255
            return blankImg
        elif color == 'red':
            blankImg[:,:,0] = 255
            return blankImg
        elif color == 'green':
            blankImg[:,:,1] = 255
            return blankImg
        elif color == 'blue':
            blankImg[:,:,2] = 255
            return blankImg
        else:
            print(f'failed to create blank image in this color: {color}')
