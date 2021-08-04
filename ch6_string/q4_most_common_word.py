import collections
import re
from _ast import List

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

"""
가장흔한단어
819. Most Common Word
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표등) 또한 무시한다.
"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        print(counts)
        print(counts.most_common(1)[0][0])
        return counts.most_common(1)[0][0]
        # counts = collections.defaultdict(int)
        # for word in words:
        #     counts[word] += 1


s = Solution()
s.mostCommonWord(paragraph, banned)
