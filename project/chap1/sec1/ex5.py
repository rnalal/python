# 셋(set) : 집합으로 순서가 없는 자료형으로 데이터 중복이 없음
# 자료의 추가, 삭제 등이 가능하고, 합집합, 차집합 등의 연산이 가능함
# { }로 값을 대입하고, 초기화함

lst1 = [80, 90, 70, 80, 60, 70]
s1 = {80, 90, 70, 80, 60, 70}       # 중복된 숫자가 출력되지 않음
s2 = {40, 70, 65, 75, 60, 85}
print("lst1 : ", type(lst1), len(lst1), lst1)
lst1 = set(lst1)    #lst1을 셋 형태로 변경
print("lst1 : ", type(lst1), len(lst1), lst1)
print("s1 : ", type(s1), len(s1), s1)
print("s1과 s2의 교집합: ", s1&s2)   #s1과 s2의 교집합이 출력됨
print("s1과 s2의 교집합: ", s1.intersection(s2))     #s1과 s2의 교집합이 출력됨
print("s1과 s2의 합집합: ", s1|s2)       #s1과 s2의 합집합이 출력됨
print("s1과 s2의 합집합: ", s1.union(s2))    #s1과 s2의 합집합이 출력됨
print("s1과 s2의 차집합: ", s1-s2)   #s1과 s2의 치집합이 출력됨
print("s1과 s2의 차집합: ", s1.difference(s2))   #s1과 s2의 치집합이 출력됨

print("s1 => ", s1)
s1.add(75)      # 원소의 추가     # s1에 75를 추가해 출력
print("add된 s1 => ", s1)
s1.update([65, 75, 85])     # 여러 원소 추가      # s1에 65, 75, 85를 추가해 출력
print("update된 s1 => ", s1)
s1.remove(75)       # 원소의 제거
print("remove된 s1 => ", s1)

#인덱스(순서)가 없으므로 슬라이딩은 할 수 없음
s1 = list(s1)   # s1을 list 형태로 변경
print("s1[1:4] => ", s1[1:4])   #슬라이딩