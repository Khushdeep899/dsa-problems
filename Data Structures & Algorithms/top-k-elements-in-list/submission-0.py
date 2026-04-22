class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict = {}
        revDict = [[] for i in range(len(nums)+1)]
        res=[]

        for n in nums:
            dict[n] = dict.get(n, 0) + 1

        for i, n in dict.items():
            revDict[n].append(i)
        
        for i in range(len(revDict)-1, 0, -1):
            for j in revDict[i]:
                res.append(j)
            
                if len(res) == k:
                    return res


        

        

        