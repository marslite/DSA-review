
if __name__ == "__main__":
    print("Graph Adjaceny List")

    love_connections = [("Lysander","Helena"), ("Hermia", "Lysander"), ("Demetries", "Hermia"), 
                        ("Helena", "Demetries"), ("Titania", "Demetries"), ("Titania", "Oberon"),
                        ("Oberon", "Titania"), ("Puck", None)]
    
    adj_lst = {}

    for source,target in love_connections:
        if source in adj_lst:
            adj_lst[source].append(target)
        adj_lst[source] = [target]
    

    print(adj_lst)

    for nbrs in adj_lst["Lysander"]:
        print(nbrs)

    for source,target  in love_connections:
        if source == "Titania":
            print(target)

