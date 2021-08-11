

"""
배열파티션 I
n개의 페이를 이용한 min(a, b)의  합으로 만들 수 있는 가장 큰 수를 출력하라.
"""
from typing import List

nums = [1,4,3,2]
output = 4


# 1. 오름차순 풀이
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        print(sum)
        return sum


# 2. 짝수 번째 값 계산
class Solution2:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sum += n

        return sum


# 3. 파이썬다운 방식
class Solution3:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


s = Solution()
s.arrayPairSum(nums)
