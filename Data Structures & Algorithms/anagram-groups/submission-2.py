class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = defaultdict(list)

        for word in strs:
            arr = [0] * 26
            for s in word:
                arr[ord(s) - ord('a')] +=1
            dict[tuple(arr)].append(word)
        
        return list(dict.values())


        