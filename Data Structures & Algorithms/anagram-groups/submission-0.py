class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We are using defaultdict because we do not want 
        # an error if a key does not exists
        result = defaultdict(list) # mapping character count with list of anagrams

        for s in strs:
            count = [0] * 26 # a - z

            for ch in s:
                count[ord(ch) - ord("a")] += 1

            # list in python can not be key in dictionary
            # that is why we are using tuple
            result[tuple(count)].append(s)
        
        return list(result.values())