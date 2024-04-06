from printBSTv import binaryTreeToStr


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    


class BST:
    def __init__(self):
        self.root = None



    def __str__(self):
        return binaryTreeToStr(self.root)
    
    def inserIterative(self,val):
        if not self.root:
            self.root = Node(val)
        else:
            prev = None
            isLeft  = None
            cur = self.root
            while(cur):
                prev = cur
                if cur.val > val:
                    isLeft = True
                    cur = cur.left
                else:
                    isLeft = False
                    cur = cur.right
            if isLeft:
                prev.left = Node(val)
            else:
                prev.right = Node(val)

                


    def insertRecursive(self,val):
        self.root = self._insertRecursive(val, self.root)

    def _insertRecursive(self, val, curNode):
        if not curNode:
            return Node(val)
        
        if curNode.val > val:
            curNode.left._insertRecursive(val, curNode.left)
        else:
            curNode.right._insertRecursive(val, curNode.right)
        
        return curNode
        




if __name__ == '__main__':
    #test cases here
    bst = BST()
    bst.inserIterative(1)
    bst.inserIterative(2)
    bst.inserIterative(3)
    bst.inserIterative(4)
    bst.inserIterative(5)
    # bst.inserIterative(6)
    # bst.inserIterative(8)
    print(bst)

    # bst = BST()
    #self.root =5
    # bst._insertRecursive(5)
    # bst._insertRecursive(3)
    # bst._insertRecursive(7)
    # bst._insertRecursive(2)
    # bst._insertRecursive(4)
    # bst._insertRecursive(6)
    # bst._insertRecursive(8)
    # print(bst)

