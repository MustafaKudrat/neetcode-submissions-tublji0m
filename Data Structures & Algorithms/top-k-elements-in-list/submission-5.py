class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        ordered = sorted(hashMap.items(), key=lambda item:item[1], reverse=True)

        sortedDict = dict(ordered)

        return list(sortedDict.keys())[:k]

# bucket sort
#def topKFrequent(self, nums: List[int], k: int) -> List[int]:
 #       count = {}
  #      freq = [[] for i in range(len(nums) + 1)]
#
 #       for num in nums:
  #          count[num] = 1 + count.get(num, 0)
   #     for num, cnt in count.items():
    #        freq[cnt].append(num)
     #   
      #  res = []
       # for i in range(len(freq) - 1, 0, -1):
        #    for num in freq[i]:
         #       res.append(num)
          #      if len(res) == k:
           #         return res