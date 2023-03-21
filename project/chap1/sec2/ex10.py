
# 비교 연산자와 논리 연산자
# 비교 연산자 : >, >=, <, <=, ==, !=
# 논리 연산자 : and, or, not

a = 30
b = 28
c = 32
print("비교 연산자")
print("a>b : ", a>b)    #크다(초과) - 후
print("a>=b : ", a>=b)  #크거나 같다(이상) - 이후
print("a<b : ", a<b)    #작다(미만) - 전
print("a<=b : ", a<=b)  #작거나 같다(이하) - 이전
print("a==b : ", a==b)  #a와 b는 같다
print("a!=b : ", a!=b)  #a는 b가 아니다

print("논리 연산자")
print("a>=30 and b<30 : ", a>=30 and b<30)
print("a<30 or b<=28 : ", a<30 or b<=28)
print("a>30 or c<30 : ", a>30 or c<30 )