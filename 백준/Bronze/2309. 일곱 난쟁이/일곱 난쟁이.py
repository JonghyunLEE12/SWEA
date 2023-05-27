
n = 9



dwarf_list = []

for i in range(9):
    dwarf_list.append(int(input()))

total = sum(dwarf_list)
faker = []
for i in range(n):
    for j in range(n):
        if dwarf_list[i] == dwarf_list[j]:
            continue
        elif total - (dwarf_list[i] + dwarf_list[j]) == 100:
            faker.append(dwarf_list[i])
            faker.append(dwarf_list[j])
    if len(faker) == 2:
        break

for dwarf in faker:
    dwarf_list.remove(dwarf)

dwarf_list.sort()

for dwarf in dwarf_list:
    print(dwarf)