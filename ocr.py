from detect import match_letter, normalize
import cv2 as cv
from pathlib import Path

def load_templates(templates_dir="templates"):
    templates = {}
    for path in Path(templates_dir).glob("*.png"):
        letter = path.stem.lower()
        img = cv.imread(str(path), cv.IMREAD_GRAYSCALE)
        templates[letter] = normalize(img)

    return templates

def ocr_board(cells, templates):
    board = [[""] * 4 for _ in range(4)]

    for row in range(4):
        for col in range(4):
            cell_img = cells[(row, col)]
            board[row][col] = match_letter(cell_img, templates)

    return board
