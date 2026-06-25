class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #[1,2,3,4]

        list1= set()

        for i in nums:
            if i in list1:
                return True
            
            list1.add(i)
            
        return False
        