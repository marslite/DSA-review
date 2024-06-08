
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        provs = 0
        #DFS is used here to explore each city and see untill when it connects.
        #The moment it does not connect anymore we know the invidual province has been visited
        #Also this ensures to not traverse over cities we have already visited before
        def dfs(curNode):
            visited.add(curNode)
            print("Len of isConnected", n)
            for j in range(n):
                if j not in visited:
                    #If we find a connection one connection from a city to another 
                    #We continue exploring on the next city in search for more connections
                    #One provice is defined by the directly or indirectly connection of cities together
                    #which form 1 single province
                    if isConnected[curNode][j] == 1:
                        dfs(j)


        for i in range(n):
            #We explore in range of the 3 arrays
            #Given that city has not been explored yet we do dfs on it
            #The moment the dfs is over which means there are no more connections 
            #from that group/single city then we know it's a province and we update 
            #our province counter. Finally we return the province counter.

            if i not in visited:
                dfs(i)
                provs += 1
        return provs
