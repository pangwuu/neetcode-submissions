class Solution:
    def isValidLine(self, line: List[str]) -> bool:
        # checks if a list is valid - i.e. check if there are duplicates
        numbers = set()
        for num in line:
            if num != '.':
                if num in numbers:
                    return False
                numbers.add(num)
        
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            if not self.isValidLine(row):
                return False

        # check columns
        for column_index in range(len(board[0])):
            column = [row[column_index] for row in board]
            if not self.isValidLine(column):
                return False

        # check boxes
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                # now we extract a 3x3 box using i and j as startpoints
                row_filtered = board[i:i + 3]
                
                box = [row[j] for row in row_filtered]

                column_2 = [row[j + 1] for row in row_filtered]
                column_3 = [row[j + 2] for row in row_filtered]
                for item in column_2:
                    box.append(item)
                for item in column_3:
                    box.append(item)

                if not self.isValidLine(box):
                    return False
        
        return True
