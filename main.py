from solve import load_dict, boardsolver

DPATH = "dict.txt"

if __name__ == "__main__":
    trie = load_dict(DPATH)

    board = [
        ['c', 'a', 't', 'x'],
        ['o', 'r', 'e', 'y'],
        ['d', 's', 'z', 'q'],
        ['w', 'x', 'y', 'z'],
    ]

    results = boardsolver(board, trie)

    for word in sorted(results, key=len, reverse=True):
        print(word)