from graphHelpers import buildAdjList


def detectCycle(adj_list):
    #O(n)
    visited = set()

    #O(N^2) runtime or O(E + V)
    #o(N) Space complexity
    for key in adj_list.keys():
        #O(n)
        if key not in visited:
            #O(n)
            if (DFS(key, set(), visited, adj_list)):
                return True
            
            # visited.add(key)
    return False


def DFS(cur_node, cur_path, visited, adj_list):
    # if cur_node in cur_path:
    #     return True
    
    cur_path.add(cur_node)
    visited.add(cur_node)

    #N
    for neighbor in adj_list[cur_node]:
        if cur_node == neighbor:
            continue
        if neighbor in cur_path:
            return True 
        
        #O(n)
        if neighbor not in visited and DFS(neighbor, cur_path, visited,adj_list):
            return True

    cur_path.remove(cur_node)
    return False





if __name__ == '__main__':
    love_conntections = [("Hermia", "Lysander"), ("Demetrius", "Lysander"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania"), ("Hermia", "Puck"), ("Puck", "Helena"),
                        ("Titania", "Titania"), ("Helena","Hermia")]
    

    adj_list = buildAdjList(love_conntections)

    print(detectCycle(adj_list))
