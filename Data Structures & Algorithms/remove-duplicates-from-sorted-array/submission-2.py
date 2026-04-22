class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        slow = 1
        fast = 1
        while fast < len(nums):
            if nums[fast] != nums[slow-1]:
                nums[slow] = nums[fast]
                slow +=1
            fast +=1
        
        return slow
        