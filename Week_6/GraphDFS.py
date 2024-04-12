from buildAdjList import buildAdjList


def DFS(adj_list,source,target):
    #In total it will be O(N^2) Runtime
    #O(n)
    visited = set()
    return _DFS(adj_list, source, target, visited)


def _DFS(adj_list,cur_node,target, visited):
    if cur_node == target:
        return True
    
    if cur_node in visited:
        return False
    
    visited.add(cur_node)
    #Will iterate in O(n)
    for neighbor in adj_list[cur_node]:
        #Will iterate in O(n)
        if (_DFS(adj_list, neighbor,target, visited)):
            return True
    return False

    


if __name__ == '__main__':
    love_connections = [("Lysander", "Helena"), ("Hermia", "Lysander"), ("Demetrius", "Lysander"),
                        ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck")]
    

    adj_list = buildAdjList(love_connections)

    # prettyPrint(love_connections)
    print(DFS(adj_list, "Hermia","Oberon"))


    words = ['cat','act','dog','tac']
    anagram = {}
    for word1 in words:
        print(word1)
        anagram[word1] = []
        for word2 in words:
            if word1 != word2:
                #if word1 equals word2 when sorted THEN they are anagrams
                if sorted(word1) == sorted(word2):
                    anagram[word1].append(word2)
    for word in anagram:
        print(word, anagram[word])

    # edges = []
    # N = 5
    # for i in range(N):
    #     for j in range(N):
    #         edges.add((i,j))

    