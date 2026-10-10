from detect import process_img
from ocr_test import load_templates, ocr_board
from solve import load_dict, boardsolver

if __name__ == "__main__":

    screenshot_path = "data/screenshots/screenshot11.png"
    dict_path = "dict.txt"


    trie = load_dict(dict_path)
    templates = load_templates()
    cells = process_img(screenshot_path)
    board = ocr_board(cells, templates)
    words = boardsolver(board, trie)
    
    for word in sorted(words, key=len, reverse=True)[:20]:
        print(word)