import collections
from typing import Deque
import re

'''
유효한 팰린드롬
125. Valid Palindrome
주어진 문자열이 팬리드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
풀이1 리스트로 변환
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs =[]
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                print(False)
                return False

        print(True)
        return True


s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")
s.isPalindrome("race a car")


'''
풀이2 데크 자료형을 이용한 최적화
'''
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                print(False)
                return False

        print(True)
        return True

'''
풀이3 슬라이싱을 사용
'''
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', ''. s)

        return s == s[::-1] # 슬라이싱
