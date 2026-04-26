class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in visited:
                return [visited[compliment], i]
            visited[nums[i]] = i

        return False
        