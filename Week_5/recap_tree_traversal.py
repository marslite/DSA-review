from BST import BinarySearchTree

def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.val)
    inorder(root.right,arr)

def reverse_inorder(root,arr):
    if root is None:
        return 
    reverse_inorder(root.right,arr)
    arr.append(root.val)
    reverse_inorder(root.left,arr)

    


def preorder(root,arr):
    if root is None:
        return
    arr.append(root.val)
    preorder(root.left,arr)
    preorder(root.right,arr)

def postorder(root,arr):
    if root is None:
        return
    postorder(root.left,arr)
    postorder(root.right,arr)   
    arr.append(root.val)



if __name__ == '__main__':
    #Initalize tree
    BST = BinarySearchTree()
    BST.put(10,10)
    BST.put(6,6)
    BST.put(15,15)
    BST.put(20,20)
    BST.put(7,7)
    BST.put(2,2)
    BST.put(4,4)
    BST.put(5,5)
    BST.put(3,3)

    # print(BST)
    arr = []
    rv_Arr = []
    pre = []
    post = []
    inorder(BST.root,arr)

    reverse_inorder(BST.root,rv_Arr)
    preorder(BST.root, pre)
    postorder(BST.root, post)
    print("Inorder:",arr)
    print("Reverse-Inorder:",rv_Arr)
    print("Preorder:",pre)
    print("Postorder:",post)

    #Inorder = [2,5,7,10,15,20]
    #reverse_inorder [20,15,10,7,5,2]

