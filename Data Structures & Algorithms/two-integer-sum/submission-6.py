class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited = {}
        """
        3:0
        4:1
        """

        #nums = 3,4,5,6

        for i in range(len(nums)):
            complement = target - nums[i] #4
            if complement in visited:
                return [visited[complement],i]
            visited[nums[i]] = i 

        return False
                


