def change(music):
    if 'A#' in music:
        music = music.replace('A#','a')
    
    if 'G#' in music:
        music = music.replace('G#','g')
    
    if 'F#' in music:
        music = music.replace('F#','f')
    
    if 'D#' in music:
        music = music.replace('D#','d')
    
    if 'C#' in music:
        music = music.replace('C#','c')
    return music

def solution(m, musicinfos):
    answer = []
    
    idx = 0
    for info in musicinfos:
        idx += 1
        
        music = info.split(',')
        start = music[0].split(':')
        end = music[1].split(':')
        
        runtime = (int(end[0])* 60 + int(end[1])) - ( int(start[0]) * 60 + int(start[1]))
        
        changed = change(music[3])
        
        a = len(changed)
        
        b = changed * ( runtime // a) + changed[:runtime%a]
        
        memo = change(m)
        
        if memo in b:
            answer.append([runtime,idx,music[2]])
    
    if len(answer) == 0:
        return '(None)'
    elif len(answer) == 1:
        return answer[0][2]
    
    else:
        answer = sorted(answer,key = lambda x : (-x[0],x[1]))
        return answer[0][2]
    