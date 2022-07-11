import sys
input = sys.stdin.readline
# 2033 반올림
# 파이썬 반올림
# 사사오입 원칙
# Round half to even(Gaussian Rounding, Banker's Rounding)
# 반올림 대상의 값이 5일 때 앞자리 숫자가 홀수면 올림, 짝수면 내림

def roundNum(k,i):
    if int(k[i]) >= 5:
        k[i-1] = str(int(k[i-1]) + 1)
        k[i] = '0'
    else:
        k[i] = '0'
        

k = list(input().rstrip())
for i in reversed(range(1,len(k))):
    roundNum(k,i)
    
print(''.join(k))





