#ivri korem 2020
"""
The Image class in the Fotofy Framework
"""

#import
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from Filters import Filters
from EditWindow import EditWindow
from Brush import Brush
from Blender import Blender

filters = Filters()
brush = Brush()
blender = Blender()

#creating the class
class Image():
    def __init__(self, path, name='myImage', width='original', height='original'):
        '''
        description
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
    
    def resize(self):
        '''
        description
        '''
        try: 
            cv.resize(self.img, (self.img.shape[1], self.img.shape[0]))
            return (self.img.shape[1], self.img.shape[0])
        except:
            print('resizing image failed')
    
    def setStyle(self, style="classic"):
        '''
        description
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
            cv.cvtColor(self.img, styleSwitcher[style])
        except:
            print("failed to set style")
        
    def applyFilter(self, filt):
        '''
        description
        '''
        if filt == 'reddify':
            filters.reddify(self.img)
        elif filt == 'blueify':
            filters.blueify(self.img)
        elif filt == 'greenify':
            filters.greenify(self.img)
        elif filt == 'blur':
            cv.imshow('blured', filters.blur(self.img))
        elif filt == 'coldChils':
            filters.coldChils(self.img)
        elif filt == 'warmVibes':
            filters.warmVibes(self.img)
        else:
            print("no valid filter specified")

    def deleteChannel(self, channel):
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
        description
        '''
        ew = EditWindow(self.img, winname, drawColor)
        ew.show(save, fileName)
    
    def createRect(self, pt1, pt2, color=(0, 255, 0), thickness=3):
        '''
        description
        '''
        brush.drawBox(self.img, pt1, pt2, color, thickness)
    
    def blendWith(self, alpha, secondImage, beta, gamma=0):
        '''
        description
        '''
        try:
            blender.blendWeightedImages(self.img, alpha, secondImage, beta, gamma)
        except:
            print('failed to blend images')
    
    def ConvertToBinary(self, threshold, maxVal):
        '''
        description
        '''
        grayImage = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        thresh, result  = cv.threshold(grayImage, threshold, maxVal, cv.THRESH_BINARY)
        return result
    
    def changeBrightness(self, gamma):
        '''
        description
        '''
        return np.power(self.img, gamma)
    
    def reduceNoiseSimple(self):
        '''
        description
        '''
        return cv.medianBlur(self.img, (5,5))
    
    def reduceNoiseComplex(self):
        '''
        description
        '''
        return cv.bilateralFilter(self.img, 9, 75, 75)
    
    def createNoise(self):
        '''
        description
        '''
        noise = np.random.randint(low=0,high=2,size=(self.imgWidth, self.imgHeight)) * 255
        grayImg = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        return cv.addWeighted(grayImg, 0.004, noise, 0.996, 0, dtype=cv.CV_64F)
        cv.waitKey(0)
    
    def show(self):
        '''
        description
        '''
        cv.imshow(self.imgName, self.img)
        cv.waitKey(0)
