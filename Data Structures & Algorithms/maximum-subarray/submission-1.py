class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cursum = 0
        maxsum = nums[0]

        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum = cursum + n
            maxsum = max(maxsum, cursum)
        

        return maxsum


