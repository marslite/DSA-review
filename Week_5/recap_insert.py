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

    def insertIterative(self,val):
        if not self.root:
            self.root = Node(val)
        else:
            prev = None
            isLeft = None
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
            

    def insertRecurisve(self,val):
        self.root = self._insertRecursive(val,self.root)

    def _insertRecursive(self,val,curNode):
        if curNode is None:
            return Node(val)
        
        if curNode.val > val:
            curNode.left = self._insertRecursive(val, curNode.left)
        else:
            curNode.right = self._insertRecursive(val, curNode.right)
        return curNode
    

        




if __name__ == "__main__":
    bst = BST()
    bst.insertIterative(5)
    bst.insertIterative(3)
    bst.insertIterative(7)
    bst.insertIterative(2)
    bst.insertIterative(4)
    bst.insertIterative(6)
    bst.insertIterative(8)
    print(bst)


    bst1 = BST()
    bst1.insertRecurisve(5)
    bst1.insertRecurisve(3)
    bst1.insertRecurisve(7)
    bst1.insertRecurisve(2)
    bst1.insertRecurisve(4)
    bst1.insertRecurisve(6)
    bst1.insertRecurisve(8)
    print(bst1)