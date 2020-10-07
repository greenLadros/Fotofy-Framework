# ivri korem 2020
"""
The EditWindow Class in the Fotofy Framework
"""

# import
import cv2 as cv
import numpy as np


class EditWindow():
    def __init__(self, img='blank', winname='myPicture', drawColor=(0, 255, 0)):
        """
        The EditWindow class is a special class only in Fotofy that allows the user to draw over and edit images.
        """
        
        # creating base vars
        self.windowName = winname
        self.drawColor = drawColor

        if img == 'blank':
            # creating black blank image
            self.img = np.zeros((500, 500, 3))
        else:
            self.img = cv.imread(img)

        # boolean to check if drawing
        self.drawingRect = False
        self.drawingStroke = False

        # tracking the initial x and y values
        self.ix = -1
        self.iy = -1

        #setting the call back function
        cv.namedWindow(winname=self.windowName)
        cv.setMouseCallback(self.windowName, self.draw)

    # creating function for drawing
    def _draw(self, event, x, y, flags, param):
        """
        private function
        """

        if event == cv.EVENT_RBUTTONDOWN:
            self.drawingRect = True
            self.ix = x
            self.iy = y

        elif event == cv.EVENT_RBUTTONUP:
            self.drawingRect = False
            cv.rectangle(self.img, (self.ix, self.iy),
                         (x, y), self.drawColor, -1)

        elif event == cv.EVENT_LBUTTONDOWN:
            self.drawingStroke = True

        elif event == cv.EVENT_LBUTTONUP:
            self.drawingStroke = False
            cv.circle(self.img, (x, y), 5, self.drawColor, -1)

        elif event == cv.EVENT_MOUSEMOVE:
            if self.drawingRect == True:
                cv.rectangle(self.img, (self.ix, self.iy),
                             (x, y), self.drawColor, -1)
            elif self.drawingStroke == True:
                cv.circle(self.img, (x, y), 5, self.drawColor, -1)

    def show(self, save=True, fileName="myPicture.jpg"):
        """
        this function opens the EditWindow

        Parameters:
        save(bool): if the image will be saved to a file after the window is closed;

        Returnes:
        Nothing;
        """
        #show the image
        while True:
            cv.imshow(self.windowName, self.img)

            # to break out of the loop press esc
            if cv.waitKey(20) & 0xFF == 27:
                break

        # saving the image
        cv.imwrite(fileName, self.img)
        # closing the window
        cv.destroyAllWindows()