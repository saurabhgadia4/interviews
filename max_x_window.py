class Window(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        if self.rows:
            self.cols = len(matrix[0])
        else:
            self.cols = 0

    def compute(self):
        max_val = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == 1:
                    max_val = 1
                    break
            if max_val:
                break
        for size in range(3, min(self.rows, self.cols) + 1, 2):
            for r in range(self.rows - size + 1):
                for c in range(self.cols - size + 1):
                    if self.is_valid(r, c, size):
                        max_val = size/2 + 1
        return max_val


    def is_valid(self, i, j, size):
        ll_r, ll_c = i, j
        lr_r, lr_c = i, j + size - 1

        for k in range(size):
            if not (self.matrix[ll_r + k][ll_c + k] and self.matrix[lr_r + k][lr_c - k]):
                return False
        return True
