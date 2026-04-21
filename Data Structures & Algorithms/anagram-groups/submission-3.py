class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for i in s:
            counts[i] = counts.get(i, 0) + 1
        for i in t:
            counts[i] = counts.get(i, 0) - 1
        for i in counts.values():
            if i!=0:
                return False
        return True
        

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     group = list()
    #     checks = dict()
    #     for i in range(len(strs)):
    #         passed = checks.get(i, False)
    #         if passed:
    #             continue
    #         else:
    #             checks[i] = True
    #             temp = [strs[i]]
    #         for j in range(i+1, len(strs)):
    #             if self.isAnagram(strs[i], strs[j]):
    #                 temp.append(strs[j])
    #                 checks[j] = True
    #         group.append(temp)
    #     return group


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedList = dict()
        for word in strs:
            k = "".join(sorted(word))
            groupedList[k] = groupedList.get(k, []) + [word]
        # print([v for k,v in groupedList.items()])
        return [v for k,v in groupedList.items()]


        