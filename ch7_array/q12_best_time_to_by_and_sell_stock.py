"""
주식을 사고팔기 가장 좋은 시점
한번의 거래로 낼 수 있는 최대 이익을 산출하라.
"""
import sys
from typing import List

nums = [7, 1, 5, 3, 6, 4]

# 1. 브루트 포스로 계산(타임아웃)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)
        print(max_price)
        return max_price


s = Solution()
s.maxProfit(nums)


#2 저점과 현재 값과의 차이 계산
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxSize

        # 최솟값과 최대값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        print(profit)
        return profit


