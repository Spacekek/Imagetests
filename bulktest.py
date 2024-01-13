# for a given folder of images, create for each image a set of 16 images of 128x128 which have been slid by 1 pixel each time
# start from the center and slide towards the top right
# before creating the images, downscale the images to 192x192

import sys
import os
import numpy as np
import cv2

def main():

    folder = sys.argv[1]

    # get list of images in folder
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), 1)
        if img is not None:
            images.append(img)

    # create folder for output, foldername_out
    outfolder = folder + "out"
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)
    
    # create 16 images for each image
    for i in range(len(images)):
        # create folder for image
        imgfolder = os.path.join(outfolder, str(i))
        if not os.path.exists(imgfolder):
            os.makedirs(imgfolder)

        # downscale image to 192x192
        images[i] = cv2.resize(images[i], (192, 192))
        for j in range(16):
            # crop image to 128x128 from center and slide towards top right
            crop = images[i][32 - j : 160 - j, 32 + j : 160 + j]
            # save image
            cv2.imwrite(os.path.join(imgfolder, str(j) + ".png"), crop)

if __name__ == "__main__":
    main()