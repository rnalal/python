
# 반복문 while
# while 조건:
#       반복실행구간
# 키보드로 작업번호를 입력받아 0이면, 작업을 종료하고,
# 1이면, 점수를 입력받음. 2이면 점수 리스트를 출력, 3이면, 합계를 구하여 출력

score = [0,0,0,0]
cnt = 0
while True:
    num = input("작업번호[0-3] :")
    if num==0 :
        print("\n작업종료")
        break
    elif num==1 :
        score[cnt] = int(input("점수 입력 : "))
        cnt+=1
    elif num==2 :
        print("/n점수 출력 : ", score)
    elif num==3 :
        i = 0
        tot = 0
        while i<cnt :
            tot+=score[i]
            i+=1
        print("n\합계 : ", tot)

# while문을 활용하여 1-100 짝수의 합계
sum = 0
i = 0
while (i<=100):
    if i % 2 == 0 :
        sum+=i
        i+=1
print("1-100 짝수의 합계:", sum)

# while문과 if문을 활용하여 10명 점수의 판정을 계산하여 출력
# 판정은 점수가 80점 이상이면, "합격", 60점 이상이면, "재평가", 60 미만이면 "탈락"

lst = [90, 70, 80, 60, 85, 75, 65, 95, 90, 80]
i = 0
while i<len(lst) :
    if lst[i]>=80 :
        print(i+1,"번째 : 합격")
    elif lst[i]>=60 :
        print(i+1,"번째 : 재평가")
    else :
        print(i+1, "번째 : 탈락")
    i+=1







