class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = dict()
        longest = 0
        l = 0

        for r, c in enumerate(s):
            if c in last_seen and l <= last_seen[c]:
                l = last_seen[c] + 1

            last_seen[c] = r
            length = r - l + 1
            longest = max(longest, length)
        
        return longest
        