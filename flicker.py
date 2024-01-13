# test image sequence for flicker and print results
# usage: python flicker.py <folder> <mask>

import sys
import os
import numpy as np
import cv2
import difference

def main():
    if len(sys.argv) != 3:
        print("usage: python flicker.py <folder> <mask>")
        return

    folder = sys.argv[1]
    mask = cv2.imread(sys.argv[2], 0)
    mask = cv2.bitwise_not(mask)

    # get list of images in folder
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), 0)
        if img is not None:
            images.append(img)

    # calculate difference
    diffs = []
    for i in range(len(images) - 1):
        diffs.append(difference(images[i], images[i + 1], mask))

    # calculate average difference
    avg = np.zeros(diffs[0].shape)
    for diff in diffs:
        avg += diff
    avg /= len(diffs)

    cv2.imshow("diff", avg)
    print("diff: ", np.sum(avg) / np.count_nonzero(avg))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()