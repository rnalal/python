# 리스트 : 여러 개의 데이터를 순서를 유지한 상태로 저장
# 리스트는 순서성이 있음(index가 있다는 것은 순서성이 있다는 것임), 데이터 중복 허용, 읽고 쓰기가 모두 가능,
# 추가, 제거, 삽입 모두 가능

lst = [90, 60, 100, 95, 80, 75, 65]
print("list=", lst)
print("lst 타입 :", type(lst))
print("lst 주소 :", id(lst))
print("lst[0] =", lst[0])       # 0번째 숫자 출력
print("lst[1:4] =", lst[1:4])   # 슬라이싱: 리스트[begin:end] -> bigin은 포함되고, end는 포함안됨
                                # 1번째부터 3번째까지 숫자 출력
print("lst[2:] =", lst[2:])     # 리스트[begin:] 2번째부터 끝까지 출력
print("lst[3:] =", lst[:3])     # 리스트[:end] 0부터 3번째 숫자까지 출력
print("lst[:] =", lst[:])       # 리스트[:] 전체 다 출력
print("lst[-2:] =", lst[-2:])   # 리스트[-begin:] 오른쪽에서 2개 숫자 출력
print("lst[:-2] =", lst[:-2])   # 리스트[:-end] 오른쪽 숫자 2개 빼고 다 출력
print("lst의 요소 수 : ", len(lst))

#리스트의 연산과 수정, 삭제
lst2 = [40, 50, 45]
print("리스트 더하기 : ", lst+lst2)       # lst뒤에 lst2 추가해서 출력됨
print("리스트 반복하기 : ", lst2*3)       # lst2가 3번 반복되어 출력됨
# lst[3] = 65       # 요소의 추가(X)
lst2.append(65)        # 요소의 추가(O)  # lst2에 65가 추가됨
lst2[1] = 60        # 요소의 값 변경     # lst2에서 1번째 값이 60으로 변경되어 출력됨
print("lst2 = ", lst2)
lst2.insert(2, 75)  #요소의 삽입     # lst2에서 2번째 자리에 75가 추가되어 출력
print("lst2 =", lst2)
lst2.sort()      # 요소의 정렬       #sort: 정렬
print("lst2 =", lst2)
lst2.reverse()      # 요소의 뒤집기   #요소의 순서가 반대로 되어 출력됨
print("lst2 = ", lst2)
print("60의 인덱스 : ", lst2.index(60))     # 60은 index에서 몇번째 자리에 있나
print("60의 요소 개수 :", lst2.count(60))    # 60의 개수
del lst2[2]      # lst에서 인덱스가 2인 숫자 삭제
print("lst2 = ", lst2)
lst2.remove(65)    # 값을 이용한 요소 제거      # lst2에서 65를 제거
print("lst2 = ", lst2)
lst2.extend([90, 70, 75])   #리스트의 확장    #lst2에 90, 70, 75 추가
print("lst2 = ", lst2)
