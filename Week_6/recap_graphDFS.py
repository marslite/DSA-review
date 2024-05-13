from buildAdjList import buildAdjList,prettyPrint


def DFS(adj_list, source, target):
    visited = set()
    #Runtime: O(N * N) = O(n^2)
    #Spacetime: O(N)
    return _DFS(adj_list, source, target, visited)

def _DFS(adj_list,cur_node, target, visited):
    if cur_node == target:
        return True
    
    if cur_node in visited:
        return False
    
    visited.add(cur_node)
    #O(N)
    for nbr in adj_list[cur_node]:
        #O(N)
        if _DFS(adj_list,nbr,target,visited):
            return True
    
    return False
    




if __name__ == '__main__':
    love_connections = [("Lysander", "Helena"), ("Hermia","Lysander"),("Demetrius","Lysander"), ("Helena","Demetrius"),("Titania","Oberon")
                        ,("Oberon", "Titania"), ("Puck","Puck"), ("Lysander", "Puck")]
    
    adj_list = buildAdjList(love_connections)

    print(DFS(adj_list,"Lysander","Puck"))
    print(DFS(adj_list,"Oberon","Puck"))

    graph_repr = prettyPrint(love_connections)


    
