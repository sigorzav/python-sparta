#########################################
# 파이썬 패키지
#########################################

#########################################
# 파이썬 가상환경
#
# 프로젝트 별로 독립적인 실행환경 구성 가능
#########################################

#########################################
# numpy
#
# 1. 선형대수나 수치계산에 강력한 도구
# 2. 예제
# >>> import numpy
# >>> numpy.array([1,2,3,4,5])
# array([1, 2, 3, 4, 5])
# >>> a = numpy.array([1,2,3,4,5])
# >>> b = [1,2,3,4,5]
# >>> a + 10
# array([11, 12, 13, 14, 15])
# >>> b + 10
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate list (not "int") to list
#
# requirements.txt
# - 오픈소스에는 기본적으로 존재
# - requirements.txt 생성
#  > pip freeze > requirements.txt
# - requirements.txt 이용한 패키지 설치 
#  > pip install -r requirements.txt
#########################################
