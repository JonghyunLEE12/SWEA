# 키 리스트 선언
key_list = []
# 난쟁이 9 명의 키를 입력
for i in range(9):
    key_list.append(int(input()))

# 가짜 난쟁이들의 키를 담을 리스트를 선언
faker = []
# 난쟁이 9명의 키의 합을 total 에 저장
total = sum(key_list)
for i in range(len(key_list)):
    for j in range(len(key_list)):
        # 본인을 두번 더하는 것을 방지
        if key_list[i] == key_list[j]:
            continue
        # 전체 난쟁이에서 두 난쟁이 키의 합을 뺀 것이 100 이라면
        # 두 난쟁이가 가짜 난쟁이
        elif total - (key_list[i]+key_list[j]) == 100:
            # 가짜 난쟁이 리스트에 저장
            faker.append(key_list[i])
            faker.append(key_list[j])
    # 중복 방지를 위해 faker 리스트의 길이가 2 면 break
    if len(faker) == 2:
        break
# i가 faker 리스트를 순회 하면서 전체 난쟁이에서 가짜 난쟁이를 제거
for i in faker:
    key_list.remove(i)
# 난쟁이의 키를 오름차순 으로 출력
key_list.sort()
for i in key_list:
    print(i)