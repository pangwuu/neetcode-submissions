class TrieNode:
    def __init__(self, char: str | None=None, terminal: bool=False) -> None:
        self.char = char
        self.terminal = terminal
        self.children: Dict[str, "TrieNode"] = {}

class WordDictionary:

    def __init__(self):
        self.startNode: TrieNode = TrieNode()

    def addWord(self, word: str) -> None:
        cursor = self.startNode
        for char in word:
            print(cursor.char)
            if char in cursor.children:
                # traverse down it
                cursor = cursor.children[char]
            else:
                # create the new TrieNode
                newNode = TrieNode(char)
                cursor.children[char] = newNode
                cursor = cursor.children[char]
            
        cursor.terminal = True
        

    def search(self, word: str) -> bool:
        return self._searchHelper(word, self.startNode)
    
    def _searchHelper(self, word: str, startNode: TrieNode) -> bool:

        cursor = startNode
        for index, char in enumerate(word):

            if char == '.':
                # special case – run this function on all the current cursor's children - like DFS? shouldn't be 
                found = False
                for child in cursor.children.values():
                    if self._searchHelper(word[index + 1:], child):
                        return True
                return False
                
            # char isn't in the children
            if char not in cursor.children:
                return False
            
            cursor = cursor.children[char]
        
        if cursor.terminal:
            return True
        
        return False
            
            


