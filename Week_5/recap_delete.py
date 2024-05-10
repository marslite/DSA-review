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
    
    def deleteRecursive(self,val):
        self.root = self._deleteRecursive(val,self.root)
    
    def _deleteRecursive(self,val,curNode):
        if curNode is None:
            return None
        
        if curNode.val < val:
            curNode.right = self._deleteRecursive(val, curNode.right)

        elif curNode.val > val:
            curNode.left = self._deleteRecursive(val, curNode.left)

        else:
            #Case 1
            if not curNode.right and not curNode.left:
                return None
            
            #Case 2 Has 2 children
            elif curNode.left and curNode.right:
                #Find smallest element in right subtree
                smallest = self.getSmallest(curNode.right)
                #delete smallest element
                curNode.right = self._deleteRecursive(smallest.val,curNode.right)

                #Now replace curNode with smallest?
                smallest.left = curNode.left
                smallest.right = curNode.right
                return smallest


            #Case 3 Has one child
            else:
                if curNode.left:
                    return curNode.left
                else:
                    return curNode.right
            
        return curNode
                
    
    def getSmallest(self, curNode):
        while(curNode.left):
            curNode = curNode.left
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

  
    bst.deleteRecursive(5)
    print(bst)
