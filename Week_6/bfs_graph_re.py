from buildAdjList import buildAdjList,prettyPrint
from queue import Queue


def BFS(adj_lst, source,target):
    Q = Queue()
    Q.put(source)
    visited = set(source)
    while(not Q.empty()):
        cur = Q.get()
        if cur == target:
            return True
        
        for nbr in adj_lst[cur]:
            if nbr not in visited:
                visited.add(nbr)
                Q.put(nbr)
    return False
            
        




if __name__ == "__main__":
    print("BFS Revision")
    love_connections = [("Lysander","Helena"), ("Hermia", "Lysander"), ("Demetrius", "Lysander"), 
                        ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena","Titania"), ("Hermia", "Puck")]
    

    adj_lst = buildAdjList(love_connections)
    print(BFS(adj_lst,"Hermia","Puck"))
    print(BFS(adj_lst,"Oberon","Puck"))


    # prettyPrint(love_connections)