from red_black_tree.r_b_tree import RedBlackTree

if __name__ == "__main__":
    rbt = RedBlackTree()

    rbt.insertNode(25)
    rbt.insertNode(10)
    rbt.insertNode(15)
    rbt.insertNode(5)
    rbt.insertNode(30)
    rbt.print_tree()
    print("\nAfter deleting an element")
    rbt.delete_node(10)
    rbt.print_tree()