class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curNode = self.root
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
            curNode = curNode.children[c]
        curNode.isWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
                
            curNode = root

            for i in range(j, len(word)):
                c = word[i]
                
                if c == ".":
                    for child in curNode.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if c not in curNode.children:
                        return False
                    curNode = curNode.children[c]

            return curNode.isWord

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)