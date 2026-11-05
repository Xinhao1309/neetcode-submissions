class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        column_maps = [{} for _ in range(9)]
        block_maps = [{} for _ in range(9)]

        for row_index, row in enumerate(board):
            row_map = {}

            if row_index in range(0, 3):
                block_base = 0
            elif row_index in range(3, 6):
                block_base = 3
            else:
                block_base = 6

            for column_index, value in enumerate(row):
                if value == ".":
                    continue

                if column_index in range(0, 3):
                    block_offset = 0
                elif column_index in range(3, 6):
                    block_offset = 1
                else:
                    block_offset = 2

                block_index = block_base + block_offset

                if value in row_map:
                    return False

                if value in column_maps[column_index]:
                    return False

                if value in block_maps[block_index]:
                    return False

                row_map[value] = 1
                column_maps[column_index][value] = 1
                block_maps[block_index][value] = 1

        return True