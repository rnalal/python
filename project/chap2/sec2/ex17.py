
# 출력 제어: print, 이스케이프문자, 형식지시자, format

name = "전재영"
age = 25
print("name=", name, "age=", age)
print("name", name, sep="=")
print("age", age, sep="=")

# 이스케이프문자 : \n, \t, \f ...
print("name=", name, "\nage=", age)

#형식지시자 : %s, %d, %f...
print("name=%s, age=%d" % (name, age))

#format 함수
print("당신의 이름은 {}이며, 나이는 {}세 입니다.".format(name, age))
print("제가 가장 좋아하는 치킨은 {1}, {0}, {2} 입니다.".format("후라이드", "양념", "간장"))
print("자바", "파이썬", "C언어", sep=" and ")

