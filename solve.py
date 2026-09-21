#Trie setup for boggle solver.

class Trie:

    #Sets up is_word, and children.
    def __init__(self):
        self.children = {}
        self.is_word = False

    #Checks to see if letter in word is a child, if it is move to that node,
    #If not, make new node with letter.
    #Then marks .is_word = true for node.
    def insert(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]
        node.is_word = True

    #Checks to see if character matches nodes
    #Returns false, if no match
    #Returns true if every character matches
    def search(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_word


#Loads dict into trie
#Trims \n, and skips empty.
def load_dict(filepath):
    trie = Trie()
    with open(filepath) as f:
        for line in f:
            word = line.strip()
            if word:
                trie.insert(word)
    return trie


#Boggle solver using DFS helper function
def boardsolver(board, trie):

    results = set()
    visited = set()

    for row_index, row in enumerate(board):
        for col_index, letter in enumerate(row):
            dfs(board, row_index, col_index, trie, "",visited, results)

    return results

#DFS helper function
def dfs(board, row, col, trie, path, visited, results):
    #out of bounds checker
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]): return

    #check if visited pos
    if (row,col) in visited: return

    #get letter from board, and check if it's in trie
    letter = board[row][col]
    if letter not in trie.children: return

    #adds to visited set
    visited.add((row,col))

    #gets path and new node.
    new_node = trie.children[letter]
    new_path = path+letter

    #if it's word adds to results
    if new_node.is_word:
        results.add(new_path)

    #dfs in adjecent squares
    for (dr,dc) in [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]:
        dfs(board,row+dr,col+dc,new_node,new_path,visited,results)

    #backtrack visited.
    visited.remove((row,col))