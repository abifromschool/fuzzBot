from detect import match_letter, normalize
import cv2 as cv
from pathlib import Path

templates = {}
for path in Path("templates").glob("*.png"):
    letter = path.stem
    img = cv.imread(str(path), cv.IMREAD_GRAYSCALE)
    templates[letter] = normalize(img)

cells = {}
for path in sorted(Path("data/tiles").glob("*.png")):
    _, row, col = path.stem.split("_")
    row, col = int(row), int(col)
    img = cv.imread(str(path), cv.IMREAD_GRAYSCALE)
    cells[(row,col)] = normalize(img)

cv.imwrite("debug_norm_cell_0_0.png", cells[(0,0)])
cv.imwrite("debug_norm_cell_1_1.png", cells[(1,1)])
cv.imwrite("debug_norm_template_R.png", templates["R"])
cv.imwrite("debug_norm_template_G.png", templates["G"])
cv.imwrite("debug_norm_template_K.png", templates["K"])
cv.imwrite("debug_norm_template_B.png", templates["B"])

board = [[""] * 4 for _ in range(4)]

for row in range(4):
    for col in range(4):
        cell_img = cells[(row, col)]
        board[row][col] = match_letter(cell_img, templates)

print(board)

for row in board:
    print("".join(row))