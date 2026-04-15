class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        create adjencency list on pattern with wild card

        bfs thru the graph
        visited, q, res
        bfs:
            layer by layer
            return res
        '''
        if endWord not in wordList:
            return 0
        graph = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                graph[pattern].append(word)
        
        res = 1
        q = deque([beginWord])
        seen = set([beginWord])

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in graph[pattern]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            res += 1
        
        return 0
