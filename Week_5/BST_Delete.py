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
        #pirnts our BST in string fromat
        return binaryTreeToStr(self.root)

    def insertRecursive(self,val):
        self.root = self._insertRecursive(val,self.root)

    def _insertRecursive(self,val, curNode):
        if not curNode:
            return Node(val)
        if curNode.val > val:
            curNode.left = self._insertRecursive(val, curNode.left)
        else:
            curNode.right = self._insertRecursive(val, curNode.right)
        
        return curNode


    def deleteRecursive(self,val):
        self.root = self._deleteReucursive(val, self.root)


    
    def _deleteReucursive(self,val,curNode):
        if curNode is None:
            return None
        
        if curNode.val < val:
            curNode.right = self._deleteReucursive(val, curNode.right)

        elif curNode.val>val:
            curNode.left = self._deleteReucursive(val, curNode.left)

        else:
            #Case 1 has no children
            if not curNode.left and not curNode.right:
                return None
            #Case3 has 2 children
            
            elif curNode.left and curNode.right:
                #find smallest element in right subtree
                smallest = self.getSmallest(curNode.right)
                #delete smallest element
                curNode.right = self._deleteReucursive(smallest.val, curNode.right)

                #Now replace curNode with smallest
                smallest.left = curNode.left
                smallest.right = curNode.right 
                return smallest

            #case2 has one child

            else:
                if curNode.left:
                    return curNode.left
                else:
                    return curNode.right
                
        return curNode
    



    def deleteRecursiveDuplicates(self,val):
        self.root = self._deleteReucursiveDuplicates(val, self.root)


    
    def _deleteReucursiveDuplicates(self,val,curNode):
        if curNode is None:
            return None
        
        if curNode.val < val:
            curNode.right = self._deleteReucursiveDuplicates(val, curNode.right)

        elif curNode.val>val:
            curNode.left = self._deleteReucursiveDuplicates(val, curNode.left)

        else:
            #Case1 has no children
            if not curNode.left and not curNode.right:
                return None
            
            #Case3 has 2 children
            elif curNode.left and curNode.right:
                #find smallest element in right subtree
                smallest = self.getSmallestAndDelete(curNode.right, curNode)
                #delete smallest element

                #Now replace curNode with smallest
                smallest.left = curNode.left
                smallest.right = curNode.right 
                return smallest

            #case2 has one child

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
    
    def getSmallestAndDelete(self,curNode, prev):
        while(curNode.left):
            prev = curNode
            curNode = curNode.left
        if prev.left is curNode:
            prev.left = curNode.right
        else:
            prev.right = curNode.right
        

        return curNode






if __name__ == '__main__':
    def makeTree():
        bst = BST()
        bst.insertRecursive(5)
        bst.insertRecursive(3)
        bst.insertRecursive(2)
        bst.insertRecursive(4)
        bst.insertRecursive(8)
        bst.insertRecursive(6)
        bst.insertRecursive(9)
        bst.insertRecursive(7)
        bst.insertRecursive(10)
        bst.insertRecursive(9)
        bst.insertRecursive(9)
        bst.root.right.right.right.val = 9


        return bst
    
    bst = makeTree()
    print(bst)

    bst.deleteRecursiveDuplicates(2)
    print(bst)

    bst.deleteRecursiveDuplicates(3)
    print(bst)

    bst.deleteRecursiveDuplicates(8)
    print(bst)

    bst.deleteRecursiveDuplicates(5)
    print(bst)

    bst.deleteRecursiveDuplicates(9)
    print(bst)

    # bst.deleteRecursiveDuplicates(9)
    # print(bst)






    # bst.deleteRecursiveDuplicates(9)
    # print(bst)

    