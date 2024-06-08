# from graphHelpers import buildAdjList,prettyPrint
from buildAdjList import buildAdjList,prettyPrint



def detectCycle(adj_list):
    visited = set()
    #Runtime O(V+E)
    for key in adj_list.keys():
        if key not in visited:
            if DFS(key, set(),visited, adj_list):
                return True
            # visited.add(key)
    return False




def DFS(cur_node, cur_path,visited, adj_list):
    if cur_node in cur_path:
        return True
    
    cur_path.add(cur_node)
    visited.add(cur_node)
    #Runtime O(N^2)
    #Runtime O(E+V)
    #Space O(N)
    for nbr in adj_list[cur_node]:
        if cur_node == nbr:
            continue
        if nbr in cur_path:
            print("Detected a Cycle!")
            return True
        
        if nbr not in visited and DFS(nbr,cur_path, visited, adj_list):
            return True

    cur_path.remove(cur_node)
    return False




if __name__ == '__main__':
    love_connections = [("Hermia", "Lysander"), ("Demetrius", "Lysander"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania"), ("Hermia", "Puck"), ("Puck", "Helena"),
                        ("Titania", "Titania")]
    


    adj_list = buildAdjList(love_connections)
    print("Does it have a cycle? ", detectCycle(adj_list))
    prettyPrint(love_connections)