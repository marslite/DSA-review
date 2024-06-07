from printBSTv import binaryTreeToStr



class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None




class BST:
    def __init__(self):
        pass

    def __str__(self):
        return binaryTreeToStr(self.root)
    
    def insertIterative(self,val):
        pass

    def insertRecursive(self,val):
        pass




if __name__ == "__main__":
    print("BST Recap")
    bst = BST()
    bst.insertIterative(5)
    bst.insertIterative(3)
    bst.insertIterative(7)
    bst.insertIterative(2)
    bst.insertIterative(6)
    bst.insertIterative(8)
    print(bst)