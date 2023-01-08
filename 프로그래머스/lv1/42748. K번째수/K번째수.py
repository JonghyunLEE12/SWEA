def solution(array, commands):
    answer = []
    for cmd in commands:
        new_array = array[cmd[0]-1:cmd[1]]
        new_array.sort()
        answer.append(new_array[cmd[2]-1])
    return answer