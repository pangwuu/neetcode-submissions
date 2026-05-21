class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(x: int, y: int, index: int, visited: List[List[int]]):
            # index represents the index of the letter of the word you're looking for
            # visited is a list of coordinates which have been previously visited
            # x and y are coordinates
            nonlocal board, word

            movements = [
                [-1, 0],
                [0, -1],
                [1, 0],
                [0, 1]
            ]

            if index >= len(word) - 1 and board[x][y] == word[index]:
                # we're done!
                return True

            if board[x][y] == word[index]:
                # this index is valid! move on to the next. We can search in all directions
                found = False

                # search all directions.
                for m in movements:
                    newX = x + m[0]
                    newY = y + m[1]

                    visited.append([x, y])
                    if newX < 0 or newX >= len(board) or newY < 0 or newY >= len(board[0]) or [newX, newY] in visited:
                        if [x, y] in visited:
                            visited.pop()
                        continue
    
                    if backtrack(newX, newY, index + 1, visited):
                        return True
                    # backtrack
                    else:
                        visited.pop()
                        
                
                return False

        
        for rowIndex in range(len(board)):
            for columnIndex in range(len(board[rowIndex])):

                if board[rowIndex][columnIndex] == word[0]:
                    
                    found = backtrack(rowIndex, columnIndex, 0, [])
                    if found:
                        return True
        
        return False
            

            