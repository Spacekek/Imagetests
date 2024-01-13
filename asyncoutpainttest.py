# test the images created for the asynchronous timewarp outpainting algorithm
# by testing the difference between outpainted edges
# takes in a folder of images which have been outpainted, these images have been slid by 1 pixel each time, 16 times
# mask is changed accordingly so only outpainted edges that are in both images are compared

import sys
import os
import numpy as np
import cv2
import difference

def main():
    outpainttest()

def outpainttest():
    # create mask with the 16th-32nd pixels on the left and bottom edges set to 1
    mask = np.zeros((192, 192), dtype=np.uint8)
    mask[160:177, 16:176] = 1
    mask[16:176, 15:32] = 1
    # get list of images in folder
    images = []
    for filename in os.listdir(sys.argv[1]):
        img = cv2.imread(os.path.join(sys.argv[1], filename), 0)
        if img is not None:
            images.append(img)

    # calculate difference
    diffs = []
    for i in range(len(images) - 1):
        # shift over mask by 1 pixel each time
        mask = np.roll(mask, 1, axis=0)
        mask = np.roll(mask, -1, axis=1)
        diffs.append(difference.difference(images[i], images[i + 1], mask))

    # calculate average difference
    avg = np.zeros(diffs[0].shape)
    for diff in diffs:
        avg += diff
    avg /= len(diffs)
    cv2.imshow("diff", avg*255)
    print("diff: ", np.sum(avg) / np.count_nonzero(avg))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()