if __name__ == "__main__":
    
    
    love_connections = [("Lysander", "Helena"), ("Hermia", "Lysander"),
                        ("Demetrius", "Hermia"), ("Helena", "Demetrius"), ("Titania", "Oberon"),
                        ("Oberon","Titania"), ("Puck", None), ("Lysander", "Puck")]

#Lysander -> Helena
#Hermia -> Lysander
#Demetrius -> Hermia
#Helena -> Demetrius
#Titania -> Oberon
#Oberon -> Titania
#Puck

adj_list =  {}

for source,target in love_connections:
    print("source", source, "target", target)
    if source in adj_list:
        print("Reached with", source )
        # print("if source", source,"in adj_list", adj_list)
        # print("adj_list[source].append(target)", adj_list[source], target)

        adj_list[source].append(target)
    else:
        # print("adj_list[source]", adj_list[source], " = target",target )
        adj_list[source] = [target]

# print(adj_list)

for neighbor in adj_list["Lysander"]:
    print(neighbor)


for source,target in love_connections:
    if source == "Lysander":
        print(target)

