import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)

        print(list(anagrams.values()))
        return list(anagrams.values())


"""
그룹 애너그램
49. Group Anagrams
문자열 배영을 받아 애너그램 단위로 그룹핑하라.
"""
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
s.groupAnagrams(a)

b = [2, 5, 1, 9, 7]
sorted(b)

