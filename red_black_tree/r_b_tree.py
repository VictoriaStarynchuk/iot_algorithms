from red_black_tree.node import Node


class RedBlackTree:
    def __init__(self):
        self.nill = Node(0)
        self.nill.color = 0
        self.nill.left = None
        self.nill.right = None
        self.root = self.nill

    def insertNode(self, val):
        node = Node(val)
        node.parent = None
        node.val = val
        node.left = self.nill
        node.right = self.nill
        node.color = 1

        y = None  # let y be the leaf
        x = self.root  # let x be the root of the tree

        while x != self.nill:  # when tree is not empty insert node
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y  # assign parent of the leaf as a new_node
        if y == None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fixInsert(node)  # call func to balance tree after insertion

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nill:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nill:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fixInsert(self, child):
        while child.parent.color == 1:  # while parent is red
            if child.parent == child.parent.parent.right:
                uncle = child.parent.parent.left  # case I
                if uncle.color == 1:
                    uncle.color = 0
                    child.parent.color = 0
                    child.parent.parent.color = 1
                    child = child.parent.parent
                else:  # case II
                    if child == child.parent.left:
                        child = child.parent
                        self.rightRotate(child)
                    child.parent.color = 0  # case III
                    child.parent.parent.color = 1
                    self.leftRotate(child.parent.parent)
            else:
                uncle = child.parent.parent.right
                if uncle.color == 1:
                    uncle.color = 0
                    child.parent.color = 0
                    child.parent.parent.color = 1
                    child = child.parent.parent
                else:
                    if child == child.parent.right:
                        child = child.parent
                        self.leftRotate(child)
                    child.parent.color = 0
                    child.parent.parent.color = 1
                    self.rightRotate(child.parent.parent)
            if child == self.root:
                break
        self.root.color = 0

    def transplant(self, x, y):
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.parent = x.parent

    def minimum(self, node):
        while node.left != self.nill:
            node = node.left
        return node

    def deleteNodeHelper(self, node, val):
        node_to_be_deleted = self.nill
        while node != self.nill:
            if node.val == val:
                node_to_be_deleted = node
            if node.val <= val:
                node = node.right
            else:
                node = node.left
        if node_to_be_deleted == self.nill:
            print("no value")
            return
        y = node_to_be_deleted
        y_original_color = y.color  # save color of node_to_delete in original_color
        if node_to_be_deleted.left == self.nill:
            x = node_to_be_deleted.right
            self.transplant(node_to_be_deleted, node_to_be_deleted.right)
        elif node_to_be_deleted.right == self.nill:
            x = node_to_be_deleted.left
            self.transplant(node_to_be_deleted, node_to_be_deleted.left)
        else:
            y = self.minimum(node_to_be_deleted.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node_to_be_deleted:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node_to_be_deleted.right
                y.right.parent = y
            self.transplant(y, y.right)
            y.left = node_to_be_deleted.left
            y.left.parent = y
            y.color = node_to_be_deleted.color
        if y_original_color == 0:
            self.fixDelete(x)

    def fixDelete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == 1:
                    sibling.color = 0
                    x.parent.color = 1
                    self.leftRotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == 0 and sibling.right.color == 0:
                    sibling.color = 1
                    x = x.parent
                else:
                    if sibling.right.color == 0:
                        sibling.left.color = 0
                        sibling.color = 1
                        self.rightRotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = 0
                    sibling.right.color = 0
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == 1:
                    sibling.color = 0
                    x.parent.color = 1
                    self.rightRotate(x.parent)
                    sibling = x.parent.left
                if sibling.right.color == 0 and sibling.left.color == 0:
                    sibling.color = 1
                    x = x.parent
                else:
                    if sibling.left.color == 0:
                        sibling.right.color = 0
                        sibling.color = 1
                        self.leftRotate(sibling)
                        sibling = x.parent.left

                    sibling.color = x.parent.color
                    x.parent.color = 0
                    sibling.left.color = 0
                    self.rightRotate(x.parent)
                    x = self.root
        x.color = 0

    def delete_node(self, key):
        self.deleteNodeHelper(self.root, key)

    def __printCall(self, node, indent, last):
        if node != self.nill:
            print(indent, end=" ")
            if last:
                print("R----", end=" ")
                indent += "     "
            else:
                print("L----", end=" ")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.val) + "(" + s_color + ")")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    def print_tree(self):
        self.__printCall(self.root, "", True)
