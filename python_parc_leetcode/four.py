class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = float("-inf")
        x = set()
        l = 0
        for r in range(len(s)):  
            if s[r] in x:  
                while l < r and s[r] in x:
                    x.remove(s[l])
                    l += 1
            x.add(s[r])
            ans = max(ans, r - l + 1)
        return ans
