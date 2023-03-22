
# 조건문 : if~, if~else~, if~elif~else~

money = True
if money :
    print("택시~! 고고씽~!")
    print("예상보다 빨리 거의 도착~!")
print("도착~!")

''' 다른 언어의 구초
if(money) {
    print("택시~! 고고씽~!")
    print("예상보다 빨리 거의 도착~!")
}
'''
score1 = int(input("1과목 점수 입력 : "))
score2 = int(input("2과목 점수 입력 : "))
score3 = int(input("3과목 점수 입력 : "))
print("1과목\t2과목\t3과목")
print(score1, score2, score3)
avg = float((score1+score2+score3)/3)

# 판정은 모든 과목이 50점 이상이고, 평균이 70이상이면 합격, 아니면 불합격
if score1>=50 and score2>=50 and score3>=50 and avg>=70 :
    print("합격")
else :
    print("불합격")

if avg>=90 :
    print("5수준\n합격")
elif avg>=80 :
    print("4수준\n합격")
elif avg>=70 :
    print("3수준\n유보")
elif avg>=60 :
    print("2수준\n불합격")
else :
    print("1수준\n불합격")

# 중첩 if
if avg>=90 :
    if score1==100 or score2==100 or score3==100 :
        print("과목만점자")
    else :
        print("전체 점수는 좋으나 해당이 되지 않습니다.")
else :
    if score1==100 or score2==100 or score3==100 :
        print("만점 과목이 있으나 전체 평균이 90이상이 아닙니다.")
    else :
        print("학습에 노력을 기울여 주시기 바랍니다. 다음 기회에")
