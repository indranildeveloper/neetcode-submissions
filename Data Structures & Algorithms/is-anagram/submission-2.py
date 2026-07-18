class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for idx in range(len(s)):
            s_map[s[idx]] = 1 + s_map.get(s[idx], 0)
            t_map[t[idx]] = 1 + t_map.get(t[idx], 0)

        return s_map == t_map