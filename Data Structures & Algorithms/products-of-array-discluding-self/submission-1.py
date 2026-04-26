class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        product = 1
        products = []

        for i in range(0, length):
            for j in range(0, length):
                if not i==j:
                    product = product * nums[j]
                
            products.append(product)
            product = 1

        return products
                
            
                


        