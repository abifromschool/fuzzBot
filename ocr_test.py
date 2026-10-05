from detect import match_letter
import cv2 as cv
from pathlib import Path

templates = {}
for path in Path("templates").glob("*.png"):
    letter = path.stem
    img = cv.imread(str(path), cv.IMREAD_GRAYSCALE)
    templates[letter] = img

cells = {}
for path in sorted(Path("data/tiles").glob("*.png")):
    _, row, col = path.stem.split("_")
    row, col = int(row), int(col)
    cells[(row,col)] = cv.imread(str(path), cv.IMREAD_GRAYSCALE)

board = [[""] * 4 for _ in range(4)]

for row in range(4):
    for col in range(4):
        cell_img = cells[(row, col)]
        board[row][col] = match_letter(cell_img, templates)

print(board)
# 4. Print as a board:
#    for row in board:
#        print(" ".join(row))

for row in board:
    print("".join(row))