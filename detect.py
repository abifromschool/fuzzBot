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

    #inner pixel offset for board
    offset = 20
    board = img[y+offset:y+h-offset, x+offset:x+w-offset]

    #get cell size
    cell_height = board.shape[0]
    cell_width  = board.shape[1]

    cell_height = cell_height // 4
    cell_width = cell_width // 4


    #sclice board into cells
    cells = []
    for row in range(4):
        for col in range (4):

            cell = board[row * cell_height:(row + 1) * cell_height, col * cell_width: (col + 1) * cell_width]
            cells.append(cell)

            cell_path = f"data/tiles/cell_{row}_{col}.png"
            cv.imwrite(cell_path, cell)



    #debug board images
    cv.imwrite("data/debug_board_tight.png", board)
    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__ == "__main__":
    main()