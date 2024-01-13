# takes 3 images and returns the difference between the first and the second using the third as a mask, resulting number is normalized to 0-1
# usage: python difference.py <image1> <image2> <mask>

import sys
import numpy as np
import cv2

def main():
    maskless = False
    if len(sys.argv) == 3:
        print ("using maskless mode")
        maskless = True
    elif len(sys.argv) != 4:
        print("usage: python difference.py <image1> <image2> <mask>")
        return

    img1 = cv2.imread(sys.argv[1], 0)
    img2 = cv2.imread(sys.argv[2], 0)
    # invert mask
    if maskless:
        mask = np.ones(img1.shape, dtype=np.uint8)
    else:
        mask = cv2.imread(sys.argv[3], 0)
        mask = cv2.bitwise_not(mask)

    diff = difference(img1, img2, mask)
    
    cv2.imshow("diff", diff*255)
    print("diff: ", np.sum(diff) / np.count_nonzero(mask))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def difference(img1, img2, mask):
    diff = cv2.absdiff(img1, img2)
    diff = cv2.bitwise_and(diff, mask)
    diff = cv2.normalize(diff, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    return diff

if __name__ == "__main__":
    main()
