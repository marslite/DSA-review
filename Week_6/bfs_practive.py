from collections import Deque

#Process current node outside of neighbors

def path_sum(root, target):
    queue = Deque([])
    queue.append((root,target))
    while queue:
        current_node, current_path_sum = queue.popleft()
        #If target == 0 return True
        if target == 0 or current_node is None:
            return True
        
        if current_path_sum == 0:
            return True
        
        if current_node is not None:
            queue.append((current_node.left, current_path_sum + current_node.val ))
            queue.append((current_node.right, current_path_sum + current_node.val ))

    return True
        

