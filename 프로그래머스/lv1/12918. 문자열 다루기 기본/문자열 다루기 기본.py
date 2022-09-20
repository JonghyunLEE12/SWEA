# def solution(s):
#     answer = True
#     if len(s) == 4 or len(s) == 6:
#         for i in s:
#             if i.isdigit():
#                 continue
#             else:
#                 return False
#     return True

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True:
            return True
        else:
            return False
    else:
        return False