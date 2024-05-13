from __future__ import annotations

# =============== BEGIN DO NOT MODIFY ========================
class Treasure:
    pass

class Monster:
    def __init__(self, name: str, damage: int):
        self.name = name 
        self.damage = damage 
        self.next = []

    def append_monster(self, monster):
        self.next.append(monster)

    def append_treasure(self, treasure: Treasure):
        self.next.append(treasure)

class Player:
    def __init__(self, health: int):
        self.health = health 
    
    def battle(self, monster: Monster):
        self.health -= monster.damage
# =============== END DO NOT MODIFY ========================

class Dungeon:
    def __init__(self, monster: Monster):
        self.monster = monster 

    # Is it possible for player to make it to the end if they start with infinite health?
    def can_at_least_one_path_make_it(self) -> bool:
      player = Player(float('inf'))      
      # result = False

      def dfs(node,player):
        #Remember that is possible to traverse the same node multiple times
        #for the sake of findings all the related paths
        visited = set()
        result = False
        to_visit = [node]

        while to_visit:
          current = to_visit.pop()
          if current not in visited:
            visited.add(current)
            if isinstance(current, Monster):
              print("Pre-Battle", player.health)
              player.battle(current)
              print("Post-Battle", player.health)

          if player.health <0:
            result = False

          if isinstance(current, Monster):
            for npc in current.next:
              if npc not in visited:
                to_visit.append(npc)
          elif isinstance(current, Treasure):
            result = True
          
        return result 

      result = dfs(self.monster, player)
      return result 




    


    # Is it possible for player to make it to end without losing all their health? 
    def can_make_it(self, player: Player) -> bool:
      #Given the example in the description, with the path (M1) -> (M4) -> (M5) -> Treasure
      #By the time M5 has been traversed/fought/discovered our player 
      #would have lost all of its HP. So the answer should be no (False)

      visited = set()
      def dfs(node,player):
        nonlocal visited
        if node not in visited:
          if isinstance(node, Treasure):
            print("Treasure found")
            return True
          else:
            print("Node we are about to add:", node.name, node.damage)
            visited.add(node)
          
        if isinstance(node, Monster):
          print("Pre-Battle:", player.health)
          player.battle(node)
          print("Post-Battle:", player.health)
          
        if player.health <0:
          return False
            
        if isinstance(node, Treasure):
          print("Treasure Found")
          return True
        # if isinstance(node, Monster):
        for neighbor in node.next:
          if dfs(neighbor,player):
            return True
        
        
        return False

      return dfs(self.monster,player)



    # Will any path make it to the end? Can they choose randomly and always make it?
    def can_all_paths_make_it(self, player: Player) -> bool:

      #Treasure first ~ Have we reached the treasure yet?
      #Are we still alive?
      #Proble here is  I cannot make to reset the player.health at the node where's is supposed to backtrack to.
      #This does not allow me to visit all the possible paths with the right health.
      #How can I overcome this?

      
      def dfs(node,player):
        to_visit = [node]

        while to_visit:
          npc  = to_visit.pop()

          print("What npc are we on?", npc.name)
          
          if hasattr(npc,'next') and not npc.next:
            print("Dead end", npc.name)
            return False
          
          if isinstance(npc, Monster):
            print("Monster", npc.name)
            print("Pre-Battle's HP", player.health)
            player.battle(npc)
            print("Post-Battle's HP" ,player.health)
            if player.health <0:
              return False
              
          
          if isinstance(npc, Treasure):
            print('Treasure Found!!!')
          
          for nextNpc in npc.next:
            if isinstance(nextNpc, Monster):
              to_visit.append(nextNpc)
              print("To visit", to_visit)
              
        return True
    
      return dfs(self.monster, player)

    # If picking paths randomly, what is the probability player will make it to the end?
    def probability_player_will_make_it(self, player: Player) -> float:
      pass