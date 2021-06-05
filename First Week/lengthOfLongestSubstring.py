
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        A = ''
        B = ''
        Max = 0
        for element in s:
            A = A + element
            B = s.lstrip()
            for element2 in A:
                if element2 in B:
                    Max = len(A)
                else:
                    continue
        return Max

s = "abcabcbb"
S = Solution()
print(S.lengthOfLongestSubstring(s))