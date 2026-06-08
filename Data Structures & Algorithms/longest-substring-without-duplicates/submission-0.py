class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        max_l = 1
        seen = set([s[l]])
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                max_l = max(max_l, r-l)
                seen.remove(s[l])
                l += 1
        return max(max_l, r-l)