class Node:
    def __init__(self):
        self.childredn = {}
        self.isWord = False



class Trie:

    def __init__(self):
        'Initialize the Trie data structure'
        self.root = Node()


    def insert(self, word: str) -> None:
        'It will insert the word by each letter into the trie '
        curNode = self.root

        for i in word:
            if i not in curNode.children:
                curNode.childredn[i] = Node()
            curNode = curNode.childredn[i]

        curNode.isWord = True


    def search(self, word:str) -> bool:
        'Returns if the word we are looking for is our Trie'
        curNode = self.root
        for c in word:
            if c in curNode.childredn:
                curNode = curNode.childredn[c]
            else:
                return False
        
        return curNode.isWord


    
    def startsWith(self, prefix: str) -> bool:
        'Returns if there is any word in the trie that starts with the given prefix'
        curNode = self.root
        condition = False
        for c in prefix:
            if c in curNode.childredn:
                curNode = curNode.childredn[c]
                condition = True
            else:
                return False
        
        return  condition


if __name__ == "__main__":
    test = Node()
    test1 = Trie()


    # test1.children['a'] = Node()
    # print(test1)

