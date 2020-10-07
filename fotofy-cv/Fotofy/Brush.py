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
        This function draws a box on an image.

        Parameters:
        img(matrix): image to draw on;
        pt1(tuple(int, int)): pt1 of the box;
        pt2(tuple(int, int)): pt2 of the box;
        color(tuple(int, int, int)): the color of the box;
        thickness(int): the thickness of the box, if equal to -1 it fills the box;

        Returnes:
        (matrix): img with the box;
        """
        try:
            return cv.rectangle(img, pt1, pt2, color, thickness)
        except:
            print('failed to draw')

    def drawCircle(self, img, center, radius=25, color=(0, 255, 0), thickness=3):
        """
        This function draws a circle on an image.

        Parameters:
        img(matrix): image to draw on;
        center(tuple(int, int)): the center of the circle;
        radius(int): the radius of the circle;
        color(tuple(int, int, int)): the color of the line;
        thickness(int): the thickness of the line, if equal to -1 it fills the line;

        Returnes:
        (matrix): img with the circle;
        """
        try:
            return cv.circle(img, center, radius, color, thickness)
        except:
            print('failed to draw')

    def drawLine(self, img, pt1 ,pt2, color=(0, 255, 0), thickness=3):
        """
        This function draws a line on an image.

        Parameters:
        img(matrix): image to draw on;
        pt1(tuple(int, int)): pt1 of the line;
        pt2(tuple(int, int)): pt2 of the line;
        color(tuple(int, int, int)): the color of the line;
        thickness(int): the thickness of the line, if equal to -1 it fills the line;

        Returnes:
        (matrix): img with the line;
        """
        try:
            return cv.line(img, pt1, pt2, color, thickness)
        except:
            print('failed to draw') 
    
    def drawText(self, img, loc, text="Hello World!", font=cv.FONT_HERSHEY_SIMPLEX, fontSize=25, color=(0, 255, 0), thickness=3):
        """
        his function draws a text on an image.

        Parameters:
        img(matrix): image to draw on;
        loc(tuple(int, int)): location of the text;
        text(string): the actual text;
        font(cv2Font): the font of the text;
        fontSize(int): the size of the text;
        color(tuple(int, int, int)): the color of the text;
        thickness(int): the thickness of the text, if equal to -1 it fills the text;

        Returnes:
        (matrix): img with the text;
        """
        try:
            return cv.putText(img, text, loc, font, fontSize, color, thickness)
        except:
            print('failed to draw')
    
    def drawPixels(self, img, pixelsMatrix, isConnected=True, color=(0, 255, 0), thickness=3):
        """
        This function draws pixels on an image.

        Parameters:
        img(matrix): image to draw on;
        pixelsMatrix(Matrix): the matrix of the pixels to draw on the image;
        isConnected(bool): a boolean that determines if the pixels will be connected by lines;
        color(tuple(int, int, int)): the color of the pixels;
        thickness(int): the thickness of the lines, if equal to -1 it fills the shape;

        Returnes:
        (matrix): img with the pixels;
        """
        try:
            vertices = np.array(pixelsMatrix, dtype=np.int32)
            pts = vertices.reshape((-1, 1, 2))
            return cv.polylines(img, [pts], isConnected, color, thickness)
        except:
            print('failed to draw')

    def createBlankImage(self, width=250, height=250, color='black'): # might chnge color from a string to the actual values
        """
        This function creates blank image.

        Parameters:
        width(int): the width of the image;
        height(int): the height of the image;
        color(string): the color you want the image to be in;

        Returnes:
        (matrix): the blank image;
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

Brush = Brush()