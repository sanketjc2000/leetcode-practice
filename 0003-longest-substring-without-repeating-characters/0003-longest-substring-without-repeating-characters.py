class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        start = 0
        maxval = 0

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[start])
                start += 1

            window.add(s[right])
            maxval = max(maxval, right - start + 1)

        return maxval

        