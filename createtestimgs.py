# from an arbitrary image, create a set of 16 images of 128x128 which have been slid by 1 pixel each time
# start from the center and slide towards the top right

import sys
import os
import numpy as np
import cv2

def main():
    if len(sys.argv) != 3:
        print("usage: python createtestimgs.py <image> <folder>")
        return

    # read as color image
    img = cv2.imread(sys.argv[1], 1)
    
    # create folder if it doesn't exist
    folder = sys.argv[2]
    if not os.path.exists(folder):
        os.makedirs(folder)

    # get middle of image
    middle = img.shape[0] // 2

    # create 16 images
    for i in range(16):
        # crop image to 128x128 from center and slide towards top right
        crop = img[middle - 64 - i : middle + 64 - i, middle - 64 + i : middle + 64 + i]
        # save image
        cv2.imwrite(os.path.join(folder, str(i) + ".png"), crop)

if __name__ == "__main__":
    main()