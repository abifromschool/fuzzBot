import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES

from detect import process_img
from ocr_test import load_templates, ocr_board
from solve import load_dict, boardsolver


dict = load_dict("dict.txt")
templates = load_templates()

def on_drop(event):

    paths = root.tk.splitlist(event.data)
    for path in paths:

        #processing
        cells = process_img(path)
        board = ocr_board(cells, templates)
        words = boardsolver(board,dict)

        #display results
        listbox.delete(0, tk.END)   # clear previous results
        for word in sorted(words, key=len, reverse=True)[:20]:
            listbox.insert(tk.END, word)

        #DEBUG print(f"Dropped: {path}")



root = TkinterDnD.Tk()


root.title("Fuzzbot")
root.geometry("400x500")

label = tk.Label(root, text="Drop a screenshot")
label.pack(fill="both", expand=True, padx=20, pady=20)

listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True, padx=20, pady=20)


label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', on_drop)

root.mainloop()