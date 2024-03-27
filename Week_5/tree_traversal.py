from BST import BinarySearchTree


#Prints out nodes in sorted order

def inorder(root,arr):
    if root is None:
        return
    
    inorder(root.left,arr)
    arr.append(root.val)
    inorder(root.right, arr)

#Prints out nodes in reverse sorted order

def reverse_inorder(root,arr):
    if root is None:
        return 
    
    reverse_inorder(root.right,arr)
    arr.append(root.val)
    reverse_inorder(root.left, arr)

def preorder(root,arr):
    if root is None:
        return
    
    arr.append(root.val)
    preorder(root.left,arr)
    preorder(root.right, arr)

def postorder(root,arr):
    if root is None:
        return
    
    postorder(root.right,arr)
    postorder(root.left,arr)
    arr.append(root.val)




if __name__ == '__main__':
    #Intialize tree
    BST = BinarySearchTree()
    BST.put(10,10)
    BST.put(6,6)
    BST.put(15,15)
    BST.put(20,20)
    BST.put(12,12)
    BST.put(7,7)
    BST.put(2,2)
    BST.put(4,4)
    BST.put(5,5)
    BST.put(3,3)
    print(BST)
    arr = []
    inorder(BST.root,arr)
    print("Inorder: ")
    print(arr)
    arr2 = []
    reverse_inorder(BST.root, arr2)
    print("Reverse Inorder:")
    print(arr2)

    arr3 = []
    preorder(BST.root, arr3)
    print("Preoder:")
    print(arr3)

    arr4 = []
    postorder(BST.root, arr4)
    print("Postorder: ")
    print(arr4)


