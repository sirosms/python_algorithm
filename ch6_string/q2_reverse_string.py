
class Solution:
    def reverseString(self, s: [str]) -> None:
        left, right = 0, len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        print(s)


class Solution2:
    def reverseString(self, s: [str]) -> None:
        s.reverse()
        print(s)

"""
문자열 뒤집기
344. Reverse String
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며
리턴없이 리스트 내부를 직접 조작하라
"""
s = Solution()
s.reverseString(["h","e","l","l","o"])

# l = List[str]
# l = ["h","e","l","l","o"]
# print(l)
