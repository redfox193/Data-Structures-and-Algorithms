from typing import Callable, List

class TrieNode:
    
    def __init__(self, size: int=256):
        """
        Initialize a TrieNode.

        Args:
            size (int): The size of the alphabet. Default is 256.
        """
        self.alpha = [None for _ in range(size)]
        self.isEndOfWord = False
        self.kolLeaf = 0


class Trie:

    def __init__(self, size: int=256, 
                 posBySymbol: Callable[[str], int]=lambda symbol: ord(symbol),
                 symbolByPos: Callable[[int], str]=lambda pos: chr(pos)):
        """
        Initialize a Trie.

        Args:
            size (int): The size of the alphabet. Default is 256.
            posBySymbol (Callable[[str], int]): A function to get the position of a symbol in the alphabet. 
                                                Default is the ASCII value of the symbol.
            symbolByPos (Callable[[int], str]): A function to get the symbol from its position in the alphabet.
                                                Default is the ASCII character corresponding to the position.
        """
        self.__size = size
        self.__root = TrieNode(self.__size)
        self.__getPosOfSymbol = posBySymbol
        self.__getSymbolByPos = symbolByPos

    def insertList(self, words: List[str]) -> None:
        """
        Insert a list of words into the Trie.

        Args:
            words (List[str]): The list of words to be inserted.
        """
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Args:
            word (str): The word to be inserted.
        """
        if word == "":
            return

        head = self.__root
        for nxt in word:
            pos = self.__getPosOfSymbol(nxt)
            if head.alpha[pos] == None:
                head.alpha[pos] = TrieNode(self.__size)
                head.kolLeaf += 1
            head = head.alpha[pos]

        head.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word is found in the Trie, False otherwise.
        """
        if word == "":
            return False
        
        head = self.__root
        for nxt in word:
            pos = self.__getPosOfSymbol(nxt)
            if head.alpha[pos] == None:
                return False
            head = head.alpha[pos]
        return head.isEndOfWord

    def startsWith(self, word: str) -> bool:
        """
        Check if there is any word in the Trie that starts with the given prefix.

        Args:
            word (str): The prefix to check.

        Returns:
            bool: True if there is a word starting with the prefix, False otherwise.
        """
        if word == "":
            return False

        head = self.__root
        for nxt in word:
            pos = self.__getPosOfSymbol(nxt)
            if head.alpha[pos] == None:
                return False
            head = head.alpha[pos]
        return True

    def remove(self, word: str) -> bool:
        """
        Remove a word from the Trie.

        Args:
            word (str): The word to be removed.

        Returns:
            bool: True if the word is successfully removed, False otherwise.
        """
        if word == "":
            return False
        
        head = self.__root
        path = []
        for nxt in word:
            pos = self.__getPosOfSymbol(nxt)
            if head.alpha[pos] == None:
                return False
            path.append((head, pos))
            head = head.alpha[pos]
        
        head.isEndOfWord = False
        while len(path) > 0:
            parent, pos = path[-1]
            head = parent.alpha[pos]
            if not head.isEndOfWord and head.kolLeaf == 0:
                parent.alpha[pos] = None
                parent.kolLeaf -= 1
            else:
                break
            path.pop()

        return True

    def getWords(self) -> List[str]:
        """
        Get a list of all the words present in the Trie.

        Returns:
            List[str]: A list of all the words in the Trie.
        """
        words = []
        self.__getWord("", self.__root, words)
        return words

    def __getWord(self, word: str, head: TrieNode, words: List[str]) -> None:
        """
        Recursive helper function to get all the words in the Trie.

        Args:
            word (str): The current word being formed.
            head (TrieNode): The current TrieNode being processed.
            words (List[str]): The list to store the words.
        """
        if head.isEndOfWord:
            words.append(word)

        if head.kolLeaf == 0:
            return
        
        for pos in range(self.__size):
            if head.alpha[pos] != None:
                self.__getWord(word + self.__getSymbolByPos(pos), head.alpha[pos], words)

    def isEmpty(self) -> bool:
        """
        Check if the Trie is empty.

        Returns:
            bool: True if the Trie is empty, False otherwise.
        """
        return self.__root.kolLeaf == 0

                
    
if __name__ == '__main__':
    trie = Trie(26, 
                lambda smb: ord(smb) - ord('a'), 
                lambda pos: chr(pos + ord('a')))
    trie.insertList(['bad', 'at', 'bed', 'ate', 'beat', 'beard'])
    print(trie.getWords())
    print(trie.search('be'))
    print(trie.startsWith('be'))
    trie.remove('bed')
    print(trie.getWords())
