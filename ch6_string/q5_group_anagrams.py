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


a = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
s.groupAnagrams(a)

b = [2, 5, 1, 9, 7]
sorted(b)

