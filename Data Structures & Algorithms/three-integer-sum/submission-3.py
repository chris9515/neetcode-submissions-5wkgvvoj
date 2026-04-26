class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                # print(i, j, k)
                temp = []
                target = -nums[i]
                if nums[j] + nums[k] == target:
                    temp.append(nums[i])
                    temp.append(nums[j])
                    temp.append(nums[k])
                    res.add(tuple(temp))
                if nums[j] + nums[k] < target:
                    j+=1
                else:
                    k -= 1
        return list(res)
