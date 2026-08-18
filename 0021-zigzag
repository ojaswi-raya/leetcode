class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        current_row = 0
        going_down = True

        for char in s:
            rows[current_row] += char

            if current_row == 0:
                going_down = True

            elif current_row == numRows - 1:
                going_down = False

            if going_down:
                current_row += 1
            else:
                current_row -= 1

        return "".join(rows)