class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(x: int, y: int, index: int, markedBoard: List[List[str]]):
            nonlocal word
            
            if index >= len(word):
                return True

            if x < 0 or y < 0 or x >= len(markedBoard) or y >= len(markedBoard[0]):
                return False

            if markedBoard[x][y] == word[index]:
                # mark as visited, explore neighbours
                markedBoard[x][y] = '#'

                found = backtrack(x + 1, y, index + 1, markedBoard) or \
                backtrack(x - 1, y, index + 1, markedBoard) or \
                backtrack(x, y + 1, index + 1, markedBoard) or \
                backtrack(x, y - 1, index + 1, markedBoard)
                
                markedBoard[x][y] = word[index]

                return found
            
            return False
        
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == word[0]:
                    found = backtrack(x, y, 0, board)
                    if found:
                        return True

        return False
            


