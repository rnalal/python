
# 반복 실행 for 내포문

lst = [90, 70, 80, 60, 85, 75, 65, 95, 90, 80]

# [조건만족시 if 조건식 else 조건거짓시 for 변수 in 컬렉션]
res = ["합격" if su>=80 else "불합격" for su in lst]
'''
for su in lst:
    if su>=80
        res.append("합격")
    else :   
        res.append("불합격") 
'''

py = [num/10 for num in lst]    # [계산식 for 변수 in 컬렉션]
'''
    for num in lst:
        py.append(num/10)
'''
for i in range(0, len(lst)):
    print("점수 :", lst[i])
    print("평점 :", py[i])
    print("판정 :", res[i])
