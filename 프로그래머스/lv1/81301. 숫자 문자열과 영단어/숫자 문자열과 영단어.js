function solution(s) {
    var answer = ''
    let words = {
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
    
    let numbers = []
    for (let i = 0; i < 10; i++){
        numbers.push(String(i))
    }
    
    let word = ''
    for (let i of s) {
        if (numbers.includes(i)) { answer += i }
        else {
            word += i
            if (words[word] !== undefined) {
                answer += words[word]
                word = ''
            }
        }
    }
    
    return Number(answer)
}