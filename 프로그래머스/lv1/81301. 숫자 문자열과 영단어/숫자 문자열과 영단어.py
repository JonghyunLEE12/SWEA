def solution(s):
    answer = ''
    words = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    numbers = [ str(x) for x in range(10)]
    word = ''
    for i in s:
        if i in numbers:
            answer += i
        else:
            word += i
            if word in words:
                answer+= words[word]
                word = ''
    answer = int(answer)
    return answer