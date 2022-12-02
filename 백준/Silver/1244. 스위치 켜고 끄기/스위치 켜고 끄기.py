switch_len = int(input())
switch_status = list(map(int, input().split()))
student_num = int(input())


for i in range(student_num):
    gender, number = map(int, input().split())

    if gender == 1:
        for idx in range(len(switch_status)):
            if (idx + 1) % number == 0:
                if switch_status[idx] == 0:
                    switch_status[idx] = 1
                else:
                    switch_status[idx] = 0

    elif gender == 2:
        idx1= number - 1
        for j in range(len(switch_status)):
            if (idx1-j) < 0 or (idx1+j) > (len(switch_status)-1):
                break
            if switch_status[idx1-j] == 0 and switch_status[idx1+j] == 0:
                switch_status[idx1-j], switch_status[idx1+j] = 1, 1
            elif switch_status[idx1-j] == 1 and switch_status[idx1+j] == 1:
                switch_status[idx1-j], switch_status[idx1+j] = 0, 0
            if switch_status[idx1-j] != switch_status[idx1+j]:
                break
for i in range((switch_len // 20) + 1):
    stat_switch_temp = switch_status[:20]
    switch_status = switch_status[20:]
    print(' '.join(list(map(str, stat_switch_temp))))