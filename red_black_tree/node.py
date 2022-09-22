# 1 - red
# 0 - black

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1                              # new node is always red
