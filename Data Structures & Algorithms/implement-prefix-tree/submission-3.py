class PrefixTreeNode:
    def __init__(self, char) -> None:
        self.char = char
        self.childNodes: List[PrefixTreeNode] = []
        self.isLastLetter = False
    
    def addChild(self, newNode) -> None:
        self.childNodes.append(newNode)
    
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

            # print(f'Looking for {char}.')
            
            if char not in [node.char for node in cursor.childNodes]:
                # create a new node - and go down that path
                # print(f'{char} has NOT been added before - adding it')
                newNode = PrefixTreeNode(char)
                cursor.addChild(newNode)
                cursor = newNode
                continue
                            
            for node in cursor.childNodes:
                # it's been added – go down that path
                
                if node.char == char:
                    # print(f'{char} has been added before')
                    cursor = node
                    break
            
        # print(f'Designating {cursor.char} as a terminal letter')
        cursor.designateTerminal()

    def search(self, word: str) -> bool:
        cursor = self.dummyRoot

        if not self.dummyRoot.childNodes:
            return False
        

        for char in word:
            
            found = False
            for node in cursor.childNodes:
                if node.char == char:
                    cursor = node
                    found = True
                    break                      
            
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
            for node in cursor.childNodes:
                if node.char == char:
                    cursor = node
                    found = True
                    break                      
            
            if not found:
                return False
        
        return True
        