class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time Complexity -> O(n)
        # Space Complexity -> O(n)
        if t == "":
            return ""
        
        countT = {}
        window = {}

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)

        have = 0
        need = len(countT)
        result = [-1, -1]
        resultLength = float("inf")
        left = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = 1 + window.get(ch, 0)

            if ch in countT and window[ch] == countT[ch]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resultLength:
                    result = [left, right]
                    resultLength = (right - left + 1)
                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        left, right = result
        return s[left:right+1] if resultLength != float("inf") else ""


