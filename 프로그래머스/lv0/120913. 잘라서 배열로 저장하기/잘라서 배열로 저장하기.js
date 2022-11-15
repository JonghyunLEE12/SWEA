function solution(my_str, n) {
    var answer = [];
    let word = ''
    for (let i of my_str) {
        if (word.length === n) {
            answer.push(word)
            word = i
        }
        else {
            word += i
        }
        
    }
    answer.push(word)
    return answer;
}