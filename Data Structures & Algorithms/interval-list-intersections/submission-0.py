class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        '''
        1> 1111111
               222222
        2> 111111111
             2222
        3> 111111
                222222
        4> 1111
                    222
        '''

        res = []
        i = j = 0
        if not firstList or not secondList:
            return []
        
        while i < len(firstList) and j < len(secondList):
            startA, endA = firstList[i]
            startB, endB = secondList[j]

            start = max(startA, startB)
            end = min(endA, endB)

            if start <= end:
                res.append([start, end])

            if endA < endB:
                i += 1
            else:
                j += 1

        return res












