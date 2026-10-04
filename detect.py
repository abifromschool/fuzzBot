import cv2 as cv
import numpy as np
import sys

def main():
    #loads screenshot into project
    img_path = "data/screenshots/screenshot1.png"

    img = cv.imread(img_path)

    if img is None:
        print(f"Failed to load {img_path}")
        sys.exit(1)

    #converts to hsv, to get border
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    l_green = np.array([45, 60, 180])
    u_green = np.array([75, 180, 255])

    #masks border within range
    mask = cv.inRange(hsv, l_green, u_green)

    #grabs contour and makes a border for cropping
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if not contours:
        print("no contours found brev")
        sys.exit()

    board_contour = max(contours, key=cv.contourArea)

    x, y, w, h = cv.boundingRect(board_contour)
    board = img[y:y+h, x:x+w]


    


    #debug board images
    cv.imshow("original", img)
    cv.imshow("green mask", mask)
    cv.imshow("board", board)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()