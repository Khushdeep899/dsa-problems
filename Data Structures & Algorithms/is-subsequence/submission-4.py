class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == t:
            return True


        # s = "node"
        #         i
        # t = "neetcode"
        #             j

        # we take the smaller string 
        # loop over chars of the smaller string
        # compare each care with a char in bigger string
        # return true if we get to end of smaller string

        i = 0
        j = 0

        while i < len(s) and j <len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
        
        return i == len(s)


    
            


  


        