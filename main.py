from solve import load_dict, boardsolver

DPATH = "dict.txt"

if __name__ == "__main__":
    print("Loading dictionary...")
    trie = load_dict(DPATH)
    print(f"Dictionary loaded. Root children: {len(trie.children)}")
    print(f"Test search for 'cat': {trie.search('cat')}")
    print(f"Test search for 'car': {trie.search('car')}")

    board = [
        ['c', 'a', 't', 'x'],
        ['o', 'r', 'e', 'y'],
        ['d', 's', 'z', 'q'],
        ['w', 'x', 'y', 'z'],
    ]

    print("Solving board...")
    results = boardsolver(board, trie)
    print(f"Found {len(results)} words")

    for word in sorted(results, key=len, reverse=True):
        print(word)