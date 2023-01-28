# def check_name(cmd,rlt):
#     print(cmd)
#     for tmp in rlt:
#         if cmd[1] in tmp:
#             name = tmp.split( )[1]
#             print(cmd[1])
#     return rlt

# def solution(record):
#     answer = []
#     rlt = []
#     for i in  record:
#         # print(cmd.split(' ')[0])
#         cmd = i.split(' ')
#         if cmd[0] == 'Enter':
#             rlt.append(f'{cmd[1]}  {cmd[2]} 님이 들어왔습니다.')
#         elif cmd[0] == 'Leave':
#             rlt = check_name(cmd,rlt)
#         elif cmd[0] == 'Change':
#             pass
#     return answer


def solution(record):
    answer = []
    dic = {}
    
    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]
            
    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %dic[sentence_split[1]])
        elif sentence_split[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %dic[sentence_split[1]])
            
    return(answer)