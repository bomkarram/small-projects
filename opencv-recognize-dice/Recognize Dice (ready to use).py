import numpy as np
import cv2


class RecognizeDice(object):
    def __init__(self, img_src):
        self.all_dice = []  # store all dice valuse

        # Read in the image
        self.__image = cv2.imread(img_src)

        # crop the box
        self.__image = self.__image[:, 147:612]

        # Make a copy of the image
        self.__image_copy = np.copy(self.__image)

        # Change color to RGB (from BGR)
        self.__image_copy = cv2.cvtColor(self.__image_copy, cv2.COLOR_BGR2RGB)

        # self.lower_dice_threshold = np.array([40, 0, 0])
        self.lower_dice_threshold = np.array([104, 79, 11])
        self.upper_dice_threshold = np.array([255, 255, 255])

        self.lower_dots_threshold = np.array([160, 134, 82])
        self.upper_dots_threshold = np.array([255, 255, 255])

        self.dice_min_area = 1200   # 1700
        self.dots_min_area = 50
        self.dots_max_area = 88


        self.apply()

    # iterate though all 6 dice and store their dots count to 'dice' list
    def apply(self):
        for d in range(6):
            try:
                self.__threshold(self.lower_dice_threshold, self.upper_dice_threshold, self.__image_copy)

                self.__find_contours()

                self.__eliminate_contours(self.dice_min_area)

                self.__select_a_dice(d)

                self.__threshold(self.lower_dots_threshold, self.upper_dots_threshold, self.__dice)

                self.__find_contours()

                self.__eliminate_contours(self.dots_min_area, self.dots_max_area)

                self.all_dice.append(self.__get_dots_number())
            except Exception as e:
                print(e)

    # Define the color threshold (mask)
    def __threshold(self, lower, upper, src):
        # Define the masked area
        self.__mask = cv2.inRange(src, lower, upper)

    # find pixels that only forms complete shape (end to end)
    # ex: square, circle ..etc
    def __find_contours(self):
        _, self.__contours, _ = cv2.findContours(self.__mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    # keep only the contours that is greater of specific size (the minimum size of dice area)
    # output should be 6
    # 1010101 is just a large number
    def __eliminate_contours(self, min_area, max_area=101010):
        # get the area of all contours
        c_area = list(map(lambda arg: cv2.contourArea(arg), self.__contours))

        # make tuple: (contour index, contour area)
        c_area = list(enumerate(c_area))

        # area_lower_bound: keep only the contours areas that is greater than area_lower_bound
        c_area = list(filter(lambda arg: max_area > arg[1] > min_area, c_area))

        # keep only the contours that its index is same as the c_area indexes; c means one contour
        self.__contours = [c for i, c in enumerate(self.__contours) if i in np.array(c_area)[:,0]]

    # Recognize a Dice - isolate specific dice
    def __select_a_dice(self, which_dice):
        self.__dice = np.copy(self.__image_copy)
        shaded_dice = np.zeros_like(self.__image_copy)

        # shade the wanted pixel with red
        cv2.drawContours(shaded_dice, self.__contours, which_dice, 255, -1)

        # maek all pixel black and keep the pixels of the shaded red area
        self.__dice[shaded_dice[:,:,0] != 255] = [0,0,0]    # NOTE: dice (3 channels)
                                                            #       shaded_dice (1 channel; we only select the RED channel - to target 255)

    def __get_dots_number(self):
        return len(self.__contours)


if __name__ == '__main__':
    recognition = RecognizeDice('images/image 02.jpg')
    print(recognition.all_dice)
    print(sum(recognition.all_dice))
