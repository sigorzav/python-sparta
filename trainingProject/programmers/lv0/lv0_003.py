# [문자열 반복해서 출력하기]
# 문자열 str과 정수 n이 주어집니다.
# str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.
#
# [제한사항]
# 1 ≤ str의 길이 ≤ 10
# 1 ≤ n ≤ 5
#
# [입출력 예]
# 입력 #1 > string 5
# 출력 #1 > stringstringstringstringstring
def strValidCheck(str):
    result = None
    if len(str) >= 1 and len(str) <= 10:
        result = str
    return result

def numValidCheck(n):
    result = None
    if n >= 1 and n <= 5:
        result = n
    return result

str = strValidCheck(input())
n = numValidCheck(int(input()))

answer = ""
if not (str == None or n == None):
    for i in range(n):
        answer += str

print(answer)