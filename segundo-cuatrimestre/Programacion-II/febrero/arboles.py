class BinaryTree:
    def __init__(self,cargo,left,right):
        self.cargo=cargo
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.cargo)

def insertBST(new_data, BST_tree):
    if BST_tree == None:
        return BinaryTree(new_data,None,None)
    else:
        if new_data<BST_tree.cargo:
            return BinaryTree(BST_tree.cargo,insertBST(new_data,BST_tree.left),BST_tree.right)
        elif new_data>BST_tree.cargo:
            return BinaryTree(BST_tree.cargo,BST_tree.left,insertBST(new_data,BST_tree.right))
        else:
            return BST_tree

