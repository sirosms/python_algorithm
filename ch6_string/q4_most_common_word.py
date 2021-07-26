import collections
import re
from _ast import List

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


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
