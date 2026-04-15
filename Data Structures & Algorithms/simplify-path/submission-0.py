class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []

        for doc in paths:
            if doc == '..':
                if stack:
                    stack.pop()
            elif doc != '.' and doc != '':
                stack.append(doc)

        return '/' + '/'.join(stack)