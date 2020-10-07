#ivri korem 2020
"""
The Blender class in the Fotofy Framework
"""

#import
import numpy as np
import cv2 as cv

#creating the class
class Blender():
    def blendImages(self, firstImage, secondImage, y_val, x_val, background='white'): # roi is region of intrest
        """
        description
        """
        x_offset = firstImage.shape()[1] + x_val
        y_offset = firstImage.shape()[0] + y_val

        #creating the roi
        roi = firstImage[y_offset:firstImage.shape()[0],x_offset:firstImage.shape()[1]]

        #converting the second img to grayscale so we can mask it
        secondImageGray = cv.cvtColor(secondImage, cv.COLOR_BGR2GRAY)

        if background == 'white':
            #inverting the mask because we want the bg to be black
            mask_inv = cv.bitwise_not(secondImageGray)
        
        #filling the gaps
        white_bg = np.full(secondImage.shape, 255, dtype=np.uint8)
        bg = cv.bitwise_or(white_bg, white_bg, mask=mask_inv)
        fg = cv.bitwise_or(secondImage, secondImage, mask=mask_inv)

        #creating the final merged roi
        final_roi = cv.bitwise_or(roi, fg)

        #merging the final roi with the full picture
        self.putOnImage(firstImage, final_roi, y_val, x_val) # notice y and x val

    def blendWeightedImages(self, firstImage, alpha, secondImage, beta, gamma=0, targetSize=(500, 500)):
        """
        description
        """
        #converting images to rgb
        img1 = cv.cvtColor(firstImage, cv.COLOR_BGR2RGB)
        img2 = cv.cvtColor(secondImage, cv.COLOR_BGR2RGB)

        #resize them to the given size
        img1 = cv.resize(img1, targetSize)
        img2 = cv.resize(img2, targetSize) 

        #returning the blended image
        try:
            return cv.addWeighted(img1, alpha, img2, beta, gamma)
        except:
            print('fails to merge images')

    def putOnImage(self, largeImage, smallImage, y_val=250, x_val=250):
        """
        description
        """
        #creating the offsets
        y_offset = largeImage.shape()[0] + y_val
        x_offset = largeImage.shape()[1] + x_val

        try:
            #merging images
            large_image[y_offset:y_offset +smallImage.shape()[0],x_offset:x_offset +smallImage.shape()[1]] = smallImage
        except:
            print('failed merging images')