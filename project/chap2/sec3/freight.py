
a = int(input("짐의 무게는 얼마입니까?"))
    if(a<10) :
        print("수수료는 없습니다.")
    else :
        res = (a//10)*10000
        print("수수료는 {:0,d}원 입니다." .format(res))