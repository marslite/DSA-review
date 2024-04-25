# from buildAdjList import buildAdjList, prettyPrint
# from queue import Queue
from buildAdjList import buildAdjList, prettyPrint
from queue import Queue


def BFS(adj_list, source, target):
    #O(N) space
    #O(N^2) Runtime
    Q = Queue()
    Q.put(source)
    visited = set(source)
    seen = set(source)

    #N
    while(not Q.empty()):
        cur = Q.get()
        if cur == target:
            return True
        #N
        for neighbor in adj_list[cur]:
            if neighbor not in seen:
                seen.add(neighbor)
                Q.put(neighbor)
    
    return False



if __name__ == '__main__':
    love_connections = [("Hermia", "Lysander"), ("Demetrius", "Lysander"),
                        ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania"), ("Hermia", "Puck"), ("Puck", "Helena")]
    

    adj_list = buildAdjList(love_connections)

    prettyPrint(love_connections)
    # print(BFS(adj_list, "Hermia","Oberon"))
    


