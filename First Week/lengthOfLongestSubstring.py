
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        A = ''
        Max = 0
        left = 0
        right = 0
        while(right < len(s)):
            if left == right:
                A = A + s[right]
                right = right + 1
                continue
            if s[right] not in A:
                A = A + s[right]
                if Max < len(A):
                    Max = len(A)
                right = right + 1
            else:
                A = A.lstrip(s[left])
                left = left + 1
        return Max



s = "abca"
S = Solution()
print(S.lengthOfLongestSubstring(s))