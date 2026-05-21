class PrefixTreeNode:
    def __init__(self, char) -> None:
        self.char = char
        self.childNodes = {}
        self.isLastLetter = False
    
    def addChild(self, newNode) -> None:
        self.childNodes[newNode.char] = newNode
    
    def designateTerminal(self):
        self.isLastLetter = True

class PrefixTree:

    def __init__(self):
        self.dummyRoot = PrefixTreeNode(None)

    def insert(self, word: str) -> None:
        cursor = self.dummyRoot
        
        for char in word:
            # does this letter exist in the root of the cursor? The idea is – has this letter in this order 
            # been added before?
            
            if char not in cursor.childNodes:
                newNode = PrefixTreeNode(char)
                cursor.addChild(newNode)
                cursor = newNode
                continue
            
            cursor = cursor.childNodes[char]
            
        cursor.designateTerminal()

    def search(self, word: str) -> bool:
        cursor = self.dummyRoot

        if not self.dummyRoot.childNodes:
            return False
        
        for char in word:
            
            found = False
            if char in cursor.childNodes:
                cursor = cursor.childNodes[char]
                found = True
                                   
            if not found:
                return False
        
        if cursor.isLastLetter:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cursor = self.dummyRoot
        
        if not self.dummyRoot.childNodes:
            return False

        for char in prefix:
            
            found = False
            if char in cursor.childNodes:
                cursor = cursor.childNodes[char]
                found = True
                                   
            if not found:
                return False
        
        return True
        