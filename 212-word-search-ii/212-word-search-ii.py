class TrieNode:
    def __init__(self):
        self.children={}
        self.word = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build the prefix tree of words
        root = TrieNode()
        for word in words:
            root.addWord(word)
            
        rows, cols = len(board), len(board[0])
        res, track = set(), set()
        
        def backtrack(r,c,node,word):
            if r<0 or c<0 or c == cols or r == rows or board[r][c] not in node.children or (r,c) in track:
                return
            
            track.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
            
            backtrack(r+1, c, node, word)
            backtrack(r-1, c, node, word)
            backtrack(r, c+1, node, word)
            backtrack(r, c-1, node, word)
            
            track.remove((r,c))
            
            
        for row in range(rows):
            for col in range(cols):
                backtrack(row,col,root,"")
        
        return res
        
        