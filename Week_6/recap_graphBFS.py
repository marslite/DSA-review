from buildAdjList import buildAdjList, prettyPrint
from queue import Queue

def BFS(adj_list, source, target):
    Q = Queue()
    Q.put(source)
    visited = set(source)
    while(not Q.empty()):
        cur = Q.get()
        if cur == target:
            return True
        for nbr in adj_list[cur]:
            if nbr not in visited:
                visited.add(nbr)
                Q.put(nbr)
    
    return False
                


#Start Hermia
#End Oberon
if __name__ == '__main__':
    love_connections = [("Lysander", "Helena"), ("Hermia","Lysander"),("Demetrius","Lysander"), ("Helena","Demetrius"),("Titania","Oberon")
                        ,("Oberon", "Titania"), ("Puck","Puck"), ("Lysander", "Puck"),("Helena","Titania"),("Hermia","Puck")]
    

    adj_list = buildAdjList(love_connections)
    prettyPrint(love_connections)
    print(BFS(adj_list, "Hermia","Oberon"))
    print(BFS(adj_list, "Titania","Puck"))

