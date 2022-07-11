import sys
input = sys.stdin.readline
# 1271 엄청난 부자2
# split의 결과 list로 반환 되므로 int로 형변환 시 타입 에러 발생
# a , b = int(input().split())

# 문자열 끝 엔터 버퍼 제거
# k = input().rstrip()

a, b = map(int, input().split())
print(a//b)
print(a%b)