
class Solution:
    def reorderLogFiles(self, logs: [str]) -> [str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)


        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

"""
로그파일 재정렬
937. Reorder Log Files
로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞부분은 식별자다
2. 문자로 구성된 로그가 숫자로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자로그는 입력순서대로 한다.
"""
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
s = Solution()
result = s.reorderLogFiles(logs)
print(result)
