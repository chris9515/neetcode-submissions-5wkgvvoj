class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        # for i in range(len(heights)-1):
        #     for j in range(i+1, len(heights)):
        #         area = (j-i)*min(heights[i], heights[j])
        #         res = max(res, area)

        left = 0
        right = len(heights)-1
        while left < right:
            area = (right-left)*min(heights[left], heights[right])
            res = max(res, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res