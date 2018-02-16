# # 
# # 1011
# # 0101
# # 1010 => 2
# # 
# # return a single int, that is the size of the largest x made of ones in the input
# # 
# # 10001
# # 01010
# # 00100
# # 01010
# # 10001 => 3
# # 
# # 
# 010000
# 001010
# 000100
# 001010
# 000000 => 2
# # 

# # 101
# # 010
# # 010 => 1
# #




def memoize_ul(fn):
    def helper(self, *args):
        if args not in self.memo_ul:
            self.memo_ul[args] = fn(self, *args)
        return self.memo_ul[args]
    return helper


def memoize_ur(fn):
    def helper(self, *args):
        if args not in self.memo_ur:
            self.memo_ur[args] = fn(self, *args)
        return self.memo_ur[args]
    return helper


def memoize_ll(fn):
    def helper(self, *args):
        if args not in self.memo_ll:
            self.memo_ll[args] = fn(self, *args)
        return self.memo_ll[args]
    return helper


def memoize_lr(fn):
    def helper(self, *args):
        if args not in self.memo_lr:
            self.memo_lr[args] = fn(self, *args)
        return self.memo_lr[args]
    return helper


class Solution(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        if self.rows:
            self.cols = len(matrix[0])
        else:
            self.cols = 0

        self.memo_ul = {}
        self.memo_ur = {}
        self.memo_ll = {}
        self.memo_lr = {}

    def compute(self):
        # compute upper left
        for i in range(self.rows - 1, -1, -1):
            for j in range(self.cols):
                if self.matrix[i][j] == 1:
                    self.traverse_ul(i, j)
                    self.traverse_ur(i, j)

        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == 1:
                    self.traverse_ll(i, j)
                    self.traverse_lr(i, j)

        max_val = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == 1:
                    ul = self.memo_ul[(i, j)]
                    ur = self.memo_ur[(i, j)]
                    ll = self.memo_ll[(i, j)]
                    lr = self.memo_lr[(i, j)]
                    max_val = max(max_val, 1 + min(ul, ur, ll, lr))
        return max_val

    @memoize_ul
    def traverse_ul(self, r, c):
        if self.is_valid(r + 1, c - 1):
            return 1 + self.traverse_ul(r + 1, c - 1)
        return 0

    @memoize_ur
    def traverse_ur(self, r, c):
        if self.is_valid(r + 1, c + 1):
            return 1 + self.traverse_ur(r + 1, c + 1)
        return 0

    @memoize_ll
    def traverse_ll(self, r, c): 
        if self.is_valid(r - 1, c - 1):
            return 1 + self.traverse_ll(r - 1, c - 1)
        return 0

    @memoize_lr
    def traverse_lr(self, r, c):
        if self.is_valid(r - 1, c + 1):
            return 1 + self.traverse_lr(r - 1, c + 1)
        return 0

    def is_valid(self, r, c):
        if r >= 0 and r < self.rows and c >= 0 and c < self.cols and self.matrix[r][c] == 1:
            return True
        return False

if __name__ == "__main__":
    # matrix = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0], [0,0,0,1,0,0], [0,0,1,0,1,0], [0,0,0,0,0,0]]
    # matrix = [[0, 1], [1, 0]]
    matrix = [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
    obj = Solution(matrix)
    print obj.compute()
