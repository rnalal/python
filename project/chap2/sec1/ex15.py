# for 변수 in 컬렉션프레임
# for 카운트변수 in range(begin, end, [step])

lst = [90, 70, 80, 60, 85, 75, 65, 95, 90, 80]
# 카운트 변수        # lst[0], lst[1]
for i in range(0, len(lst)):    # range(begin, end), i : 0~9 (lst의 인덱스)
    if lst[i]>=80:
        print(i+1, "번째 판정 : 합격")
    else :
        print(i + 1, "번째 판정 : 불합격")
#데이터 변수     #90, 70, 80
for jum in lst:
    if jum>=80 :
        print("합격")
    else :
        print("불합격")

# for~in~range~를 활용하여 0~100의 5의 배수의 합계를 계산하라

sum = 0
for i in range(0,101,5):      # range(begin,end,step)
        sum+=i
print("0-100의 5의 배수의 합계1 : ", sum)

sum = 0
for i in range(0,int(100/5)+1): #5의 배소의 개수 만큼 실행
    sum+=i*5
print("0~100의 합계2 : ", sum)

