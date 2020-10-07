#ivri korem 2020
"""
The Image class in the Fotofy Framework
"""

#import
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from Fotofy.Filters import Filters
from Fotofy.EditWindow import EditWindow
from Fotofy.Brush import Brush
from Fotofy.Blender import Blender

filters = Filters()
brush = Brush()
blender = Blender()

#creating the class
class Image():
    def __init__(self, path, name='myImage', width='original', height='original'):
        '''
        the image class: you can give it an image and it will give you access to
        alot of usefull methods;
        '''
        #setting basic vars
        self.imgPath = path
        self.imgName = name
        self.imgWidth = width
        self.imgHeight = height

        #getting the image and modifying it
        try:
            self.img = cv.imread(self.imgPath)
        except:
            print("Failed Reading image")
        
        if width == 'original' or height == 'original':
            self.imgWidth, self.imgHeight, c = np.shape(self.img)
        else:
            try:
                self.resize(self.imgWidth, self.imgHeight)
            except:
                print("resizing image failed")
    
    def resize(self, width, height):
        '''
        this fuction resizes the image

        Parameters:
        width(int): the target width of the image;
        height(int): the target height of the image;

        Returnes:
        (int, int): (width, height)
        '''
        try: 
            cv.resize(self.img, (height, width))
            return (width, height)
        except:
            print('resizing image failed')
    
    def setStyle(self, style="classic"):
        '''
        this fuction sets the style of the image

        Parameters:
        style(string): the target style or cv2COLOR of the image(no capital letters);

        Returnes:
        (matrix): the image after the change;
        '''
        if style == "classic":
            #if no input :
            return
        styleSwitcher = {
            'bgr2gray': cv.COLOR_BGR2GRAY,
            'bgr2rgb': cv.COLOR_BGR2RGB,
            'bgr2rgba': cv.COLOR_BGR2RGBA,
            'rgb2bgr': cv.COLOR_RGB2BGR,
            'rgb2gray': cv.COLOR_RGB2GRAY,
            'rgb2bgra': cv.COLOR_RGB2BGRA,
            'gray2bgr': cv.COLOR_GRAY2BGR,
            'gray2rgb': cv.COLOR_GRAY2RGB,
            'gray2bgra': cv.COLOR_GRAY2BGRA,
            'gray2rgba': cv.COLOR_GRAY2RGBA
        }
        try:
            return cv.cvtColor(self.img, styleSwitcher[style])
        except:
            print("failed to set style")
        
    def applyFilter(self, filt):
        '''
        this fuction applies a filter on the image
        Parameters:
        filt(string): the target filter or FotofyFilter;

        Returnes:
        (matrix): the image after the change;
        '''
        if filt == 'reddify':
            return filters.reddify(self.img)
        elif filt == 'blueify':
            return filters.blueify(self.img)
        elif filt == 'greenify':
            return filters.greenify(self.img)
        elif filt == 'blur':
            return cv.imshow('blured', filters.blur(self.img))
        elif filt == 'coldChils':
            return filters.coldChils(self.img)
        elif filt == 'warmVibes':
            return filters.warmVibes(self.img)
        else:
            print("no valid filter specified")

    def deleteChannel(self, channel):
        """
        this fuction deletes one of the image channels

        Parameters:
        channel(string): the target rgb channel of the image(no capital letters);

        Returnes:
        Nothing;
        """
        try:
            if channel == 'red':
                self.img[:,:,0] = 0
            elif channel == 'green':
                self.img[:,:,1] = 0
            elif channel == 'blue':
                self.img[:,:,2] = 0
            else:
                print("no such chanell") #maybe need to add some channels
        except:
            print('Failed to delete channel')
    
    def maximizeChannel(self, channel):
        """
        this fuction maximizes one of the image channels

        Parameters:
        channel(string): the target rgb channel of the image(no capital letters);

        Returnes:
        Nothing;
        """
        try:
            if channel == 'red':
                self.img[:,:,0] = 255
            elif channel == 'green':
                self.img[:,:,1] = 255
            elif channel == 'blue':
                self.img[:,:,2] = 255
            else:
                print("no such chanell:" + channel) #maybe need to add some channels
        except:
            print('Failed to delete channel')
        
    def openInEditWindow(self, winname="myPicture", drawColor=(0, 255, 0), save=True, fileName='myPicture.jpg'):
        '''
        this fuction opens the image in an edit window from the EditWindow class

        Parameters:
        winname(string): the window name;
        drawColor(tuple(int, int, int)): the target draw color;
        save(bool): if the image is going to be saved to file or not;
        fileName(string): in case that save equals true, the target file name and type;

        Returnes:
        Nothing;
        '''
        ew = EditWindow(self.img, winname, drawColor)
        ew.show(save, fileName)
    
    def createRect(self, pt1, pt2, color=(0, 255, 0), thickness=3):
        '''
        this fuction draws a box on an the image using the Brush class

        Parameters:
        pt1(tuple(int, int)): pt1 of the box;
        pt2(tuple(int, int)): pt2 of the box;
        color(tuple(int, int, int)): the color of the box;
        thickness(int): the thickness of the box, if equal to -1 it fills the box;

        Returnes:
        (matrix): img with the box;
        '''
        return brush.drawBox(self.img, pt1, pt2, color, thickness)
    
    def blendWith(self, alpha, secondImage, beta, gamma=0):
        '''
        This function blends images based on weight values, using the Blender class.

        Parameters:
        alpha(int): the weight of the first image;
        secondImage(matrix): BGR image to blend onto firstImage;
        beta(int): the weight of the second image;
        gamma(int): optional weight value;
        size(tuple(int, int)): the final size the final image will be in;

        Returnes:
        (matrix): The Final image;
        '''
        try:
            return blender.blendWeightedImages(self.img, alpha, secondImage, beta, gamma)
        except:
            print('failed to blend images')
    
    def ConvertToBinary(self, threshold, maxVal):
        '''
        This converts image to black and white.

        Parameters:
        threshold(int): the threshold of the image;
        maxVal(matrix): the max value of the image;

        Returnes:
        (matrix): The result;
        '''
        grayImage = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        thresh, result  = cv.threshold(grayImage, threshold, maxVal, cv.THRESH_BINARY)
        return result
    
    def changeBrightness(self, gamma):
        '''
        this function changes the brightness of the image using,
        gamma correction.

        Parameters:
        gamma(int): if gama is less then one the image will be darker and if higher it will be brighter;

        Returnes:
        (matrix): the result;
        '''
        return np.power(self.img, gamma)
    
    def reduceNoiseSimple(self):
        '''
        this function reduces noise if its simple

        Parameters:
        Nothing;

        Returnes:
        (matrix): the result;
        '''
        return cv.medianBlur(self.img, (5,5))
    
    def reduceNoiseComplex(self):
        '''
        this function reduces noise if its simple or complex but takes more time then the first one

        Parameters:
        Nothing;

        Returnes:
        (matrix): the result;
        '''
        return cv.bilateralFilter(self.img, 9, 75, 75)
    
    def createNoise(self):
        '''
        this function creates noise on the image;

        Parameters:
        Nothing;

        Returnes:
        (matrix): the result;
        '''
        noise = np.random.randint(low=0,high=2,size=(self.imgWidth, self.imgHeight)) * 255
        grayImg = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        return cv.addWeighted(grayImg, 0.004, noise, 0.996, 0, dtype=cv.CV_64F)
        cv.waitKey(0)
    
    def applyKernel(self, kernel):
        '''
        this function applies the given kernel on the picture

        Parameters:
        kernel(matrix): the kernel;

        Returnes:
        (matrix): the result;
        '''
        return cv.filter2D(self.img, -1, kernel)
    
    def show(self):
        '''
        this function displays the image;

        Parameters:
        Nothing;

        Returnes:
        Nothing;
        '''
        cv.imshow(self.imgName, self.img)
        cv.waitKey(0)
