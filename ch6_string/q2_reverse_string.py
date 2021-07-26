


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

s = Solution()
s.reverseString(["h","e","l","l","o"])

# l = List[str]
# l = ["h","e","l","l","o"]
# print(l)
