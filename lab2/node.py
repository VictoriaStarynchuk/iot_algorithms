class Node:
    # (x, y) represents coordinates of a cell in the matrix
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_dist(self):
        return self.dist


# These arrays are used to get row and column numbers of 4 neighbours of a given cell
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


# The function returns false if (x, y) is not on valid position and if vale is correct)
def is_valid(x, y, width, height):
    if height > x >= 0 and width > y >= 0:
        return True
    else:
        return False
