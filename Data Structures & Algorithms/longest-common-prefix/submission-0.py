class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(s) for s in strs])

        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1

        return strs[0][:i]