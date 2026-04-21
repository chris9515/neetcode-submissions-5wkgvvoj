class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = dict()
        for num in nums:
            res[num] = res.get(num, 0) + 1
        countMap = [[] for _ in range(len(nums)+1)]
        for t,v in res.items():
            countMap[v].append(t)
        freq = list()
        for i in range(len(countMap)-1, -1, -1):
            for num in countMap[i]:
                freq.append(num)
                if len(freq) == k:
                    return freq
        return freq

        
        