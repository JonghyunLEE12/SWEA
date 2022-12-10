key_list = []
for i in range(9):
    key_list.append(int(input()))
faker = []
total = sum(key_list)
for i in range(len(key_list)):
    for j in range(len(key_list)):
        if key_list[i] == key_list[j]:
            continue
        elif total - (key_list[i]+key_list[j]) == 100:
            faker.append(key_list[i])
            faker.append(key_list[j])
    if len(faker) == 2:
        break
faker = set(faker)
for i in faker:
    key_list.remove(i)
key_list.sort()
for i in key_list:
    print(i)