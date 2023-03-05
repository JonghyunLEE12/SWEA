# def solution(wallpaper):
#     answer = [50, 50, 0, 0]
#     for yi, y in enumerate(wallpaper):
#         for xi, x in enumerate(y):
#             if x == '#':
#                 answer = [
#                             min(answer[0], yi), min(answer[1], xi),
#                             max(answer[2], (yi+1)), max(answer[3], (xi+1))
#                          ]
#     return answer




def solution(wallpaper):
    answer = [50,50,0,0]
    
    for y_idx,y in enumerate(wallpaper):
        for x_idx,x in enumerate(y):
            if x == '#':
                answer = [
                    min(answer[0],y_idx),min(answer[1],x_idx),
                    max(answer[2],(y_idx+1)),max(answer[3],(x_idx+1))
                ]
    return answer
