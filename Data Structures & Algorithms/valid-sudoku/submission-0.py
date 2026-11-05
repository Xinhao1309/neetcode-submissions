class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # one hashmap rows
        # one list of hashmaps for all columns
        # one list of hashmaps for all boxes
        column_hm = [defaultdict() for _ in range(9)] # list comprehension 
        block_hm = [defaultdict() for _ in range(9)]
        row_counter = 0
        block_counter = 0
        for row in board:
            row_hm = defaultdict()
            column_counter = 0
  
            if row_counter in range (0, 3):
                block_counter = 0
            elif row_counter in range (3, 6):
                block_counter = 3
            else:
                block_counter = 6
            block_counter_offset = 0
            for column_value in row:
                if column_value != ".":
                    if column_value in row_hm :
                        return False
                    else:
                        row_hm[column_value] = 1

                    if column_value in column_hm[column_counter]:
                        return False
                    else:
                        column_hm[column_counter][column_value] = 1
                    
                    if column_counter in range(0,3):
                        block_counter_offset = 0
                    elif column_counter in range(3, 6):
                        block_counter_offset = 1
                    else:
                        block_counter_offset = 2

                    if column_value in block_hm[block_counter + block_counter_offset]:
                        return False
                    else:
                        block_hm[block_counter + block_counter_offset][column_value] = 1

                column_counter += 1

            row_counter += 1

        return True
                
                
                

                
                