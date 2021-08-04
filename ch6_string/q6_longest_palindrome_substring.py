"""
가장 긴 팰린드롬 부분 문자열
가장 긴 팰린드롬 부분 문자열을 출력하라.
"""
"""
hotfixes branch
"""

input_value = "babad"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        for i in range(0, len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len
                         )
        print(result)
        return result


s = Solution()
s.longestPalindrome(input_value)
